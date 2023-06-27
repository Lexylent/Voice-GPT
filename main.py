from flask import Flask, jsonify, render_template, request, send_from_directory
from server_control import stop_previous_instance, start_new_instance
import webbrowser
from audio import record_audio, transcribe_audio
from api_service import generate_answer
from database import create_tables, insert_recording
from garbage_collector import start_garbage_collector

# Portnummer, die Sie verwenden möchten
port = 5000

# Überprüfen und Beenden der vorherigen Instanz
stop_previous_instance(port)

# Starten der neuen Instanz
start_new_instance(port)

app = Flask(__name__)

# Index-Seite
@app.route('/')
def index():
    return render_template('index.html')


# Setze den Flask-Server als globalen Thread
flask_server_thread = None


#Diese Funktion wird aufgerufen, wenn eine POST-Anfrage an /exit gesendet wird.
#Sie beendet den Flask-Server und gibt den Text "Programm beendet" zurück.


@app.route('/exit', methods=['POST'])
def exit_program():
    
    print("Das Programm wurde beendet")
    shutdown_flask_server()  # Flask-Server beenden
    return 'Programm beendet'  # Textausgabe


# Diese Funktion startet den Flask-Server auf Port 5000.

def run_flask_server():
    
    app.run(port=5000)

def shutdown_flask_server():
    
   # Diese Funktion wird verwendet, um den Flask-Server ordnungsgemäß zu beenden.
    
    func = request.environ.get('werkzeug.server.shutdown')
    if func is not None:
        func()  # Ruft die Funktion zum Beenden des Flask-Servers auf



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

    global conversation_state  # Zugriff auf die globale Konversationszustandsvariable
    response = generate_answer(f"{correction}\nZustand: {conversation_state}")

    # Extrahiere den Text der Antwort und den aktualisierten Konversationszustand
    if response:
        answer = response.strip()
        conversation_state = f"Zustand: {conversation_state}"
    else:
        answer = 'Keine Antwort gefunden.'

    return jsonify({'response': answer})
# CSS-Datei
@app.route('/templates/styles.css')
def serve_css():
    return send_from_directory('templates', 'styles.css', mimetype='text/css')

# JavaScript-Datei
@app.route('/templates/scripts.js')
def serve_script():
    return send_from_directory('templates', 'scripts.js')


# Starten der neuen Instanz
start_new_instance(port)




# Öffne einen Tab im Browser und starte die App
if __name__ == '__main__':
    create_tables()  # Tabellen in der Datenbank erstellen
    start_garbage_collector()  # Startet den garbage_collector in einem separaten Thread.
    webbrowser.open('http://127.0.0.1:5000')
    app.run(port=5000, debug=False)
