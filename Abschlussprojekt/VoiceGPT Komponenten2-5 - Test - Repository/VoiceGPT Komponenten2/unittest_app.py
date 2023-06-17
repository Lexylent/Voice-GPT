import unittest
from flask import Flask
from main import app


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

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

if __name__ == '__main__':
    unittest.main()
