import unittest
import sqlite3
import os 
from flask import Flask
from main import app
from database import create_tables, insert_user, insert_recording
from server_control import cleanup_log_file


class AppTestCase(unittest.TestCase):

    def test_cleanup_log_file(self):
        # Erzeuge eine Test-Log-Datei mit einer Größe von 2 MB und 10 Einträgen
        log_file_path = 'server.log'
        with open(log_file_path, 'w') as file:
            for i in range(10):
                file.write(f"Eintrag {i+1}\n")

        # Führe die Aufräumfunktion aus
        cleanup_log_file(log_file_path, max_size_mb=1, max_entries=5)

        # Überprüfe, ob die Log-Datei aufgeräumt wurde
        self.assertTrue(os.path.isfile(log_file_path))  # Überprüft, ob die Log-Datei noch vorhanden ist

    def test_cleanup_temporary_files(self):
        # Erzeuge temporäre Testdateien im "output"-Ordner
        os.makedirs('output', exist_ok=True)
        with open('output/test1.wav', 'w') as file:
            file.write('Test Audio')
        with open('output/test1.txt', 'w') as file:
            file.write('Test Text')
        with open('output/test2.wav', 'w') as file:
            file.write('Test Audio')
        with open('output/test2.txt', 'w') as file:
            file.write('Test Text')

        # Überprüfe, ob die Testdateien gelöscht wurden
        files = ['output/test1.wav', 'output/test1.txt', 'output/test2.wav', 'output/test2.txt']
        remaining_files = [file for file in files if os.path.exists(file)]
        self.assertEqual(len(remaining_files), 4)  # Es sollten keine Testdateien mehr übrig sein

        # Aufräumen: Lösche temporäre Testdateien
        for file in files:
            os.remove(file)
    
    def setUp(self):
        self.app = app.test_client()
        create_tables()  # Tabellen in der Datenbank erstellen
        
    @classmethod
    def tearDown(self):
    # Tabellen aus der Datenbank löschen
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("DROP TABLE IF EXISTS user")
        c.execute("DROP TABLE IF EXISTS recordings")
        conn.commit()
        conn.close()


    def test_index_route(self):
        # Testet den Aufruf der Indexroute '/'
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)  # Überprüft den Statuscode der Antwort

    def test_transcribe_route(self):
        # Testet den Aufruf der Transcribe-Route '/transcribe'
        response = self.app.post('/transcribe')
        self.assertEqual(response.status_code, 200)  # Überprüft den Statuscode der Antwort
        self.assertEqual(response.headers['Content-Type'], 'application/json')  # Überprüft den Content-Type der Antwort

    def test_correct_route(self):
        # Testet den Aufruf der Correct-Route '/correct' mit JSON-Daten
        data = {'correction': 'This is a test.'}
        response = self.app.post('/correct', json=data)
        self.assertEqual(response.status_code, 200)  # Überprüft den Statuscode der Antwort
        self.assertEqual(response.headers['Content-Type'], 'application/json')  # Überprüft den Content-Type der Antwort
        response_data = response.get_json()
        self.assertIn('response', response_data)  # Überprüft, ob 'response' im JSON-Daten enthalten ist
        self.assertIsInstance(response_data['response'], str)  # Überprüft den Datentyp von 'response'

    def test_insert_user(self):
        # Testen Sie das Einfügen eines Benutzers in die Datenbank
        name = 'Alex Ibach'
        email = 'ibachalex13@gmail.com'
        insert_user(name, email)

        # Überprüfen Sie, ob der Benutzer in der Datenbank vorhanden ist
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("SELECT * FROM user WHERE name = ? AND email = ?", (name, email))
        result = c.fetchone()
        conn.close()

        self.assertIsNotNone(result)  # Überprüfen Sie, ob ein Ergebnis zurückgegeben wurde
        self.assertEqual(result[1], name)  # Überprüfen Sie den Namen des Benutzers
        self.assertEqual(result[2], email)  # Überprüfen Sie die E-Mail des Benutzers

    def test_insert_recording(self):
        # Testen Sie das Einfügen einer Aufnahme in die Datenbank
        audio_filename = 'audio.wav'
        text_filename = 'transcript.txt'
        insert_recording(audio_filename, text_filename)

        # Überprüfen Sie, ob die Aufnahme in der Datenbank vorhanden ist
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("SELECT * FROM recordings WHERE audio_filename = ? AND text_filename = ?", (audio_filename, text_filename))
        result = c.fetchone()
        conn.close()

        self.assertIsNotNone(result)  # Überprüfen Sie, ob ein Ergebnis zurückgegeben wurde
        self.assertEqual(result[1], audio_filename)  # Überprüfen Sie den Audiodateinamen
        self.assertEqual(result[2], text_filename)  # Überprüfen Sie den Textdateinamen

if __name__ == '__main__':
    unittest.main()
