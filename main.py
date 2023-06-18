from flask import Flask, jsonify, render_template, request, send_from_directory
import webbrowser
from audio import record_audio, transcribe_audio
from api_service import generate_answer
from database import create_tables, insert_recording
from garbage_collector import start_garbage_collector

app = Flask(__name__)

# Index-Seite
@app.route('/')
def index():
    return render_template('index.html')

# Route zum Transkribieren des aufgenommenen Audios
@app.route('/transcribe', methods=['POST'])
def transcribe():
    output_filename, text_file = record_audio()

    if output_filename is None:
        error_message = 'Fehler: Kein Mikrofon angeschlossen. Bitte ein Mikrofon anschließen und erneut versuchen.'
        text = "Error: " + error_message
        return jsonify({'error': error_message, 'text': text}), 500

    text = transcribe_audio(output_filename, text_file)

    if not text:
        error_message = 'Fehler bei der Spracherkennung. Bitte erneut versuchen.'
        text = "Error: " + error_message
        return jsonify({'error': error_message, 'text': text}), 500

    # Überprüfe, ob die Spracherkennung fehlgeschlagen ist
    if text is None:
        return jsonify({'error': 'Fehler bei der Spracherkennung. Bitte erneut versuchen.'}), 500

    insert_recording(output_filename, text_file)  # Hinzufügen der Aufnahme in die Datenbank

    return jsonify({'text': text})

# Route zur Fragestellung an die OpenAi API
@app.route('/correct', methods=['POST'])
def generate_answer_route():
    data = request.get_json()
    correction = data['correction']
    response = generate_answer(correction)
    return jsonify({'response': response})

# CSS-Datei
@app.route('/templates/styles.css')
def serve_css():
    return send_from_directory('templates', 'styles.css', mimetype='text/css')

# JavaScript-Datei
@app.route('/templates/scripts.js')
def serve_script():
    return send_from_directory('templates', 'scripts.js')

# Öffne einen Tab im Browser und starte die App
if __name__ == '__main__':
    create_tables()  # Tabellen in der Datenbank erstellen
    start_garbage_collector()  # Startet den garbage_collector in einem separaten Thread.
    webbrowser.open('http://127.0.0.1:5000')
    app.run(port=5000)
