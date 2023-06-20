import unittest
import sqlite3
from flask import Flask
from main import app
from database import create_tables, insert_user, insert_recording

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        create_tables()  # Tabellen in der Datenbank erstellen

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
