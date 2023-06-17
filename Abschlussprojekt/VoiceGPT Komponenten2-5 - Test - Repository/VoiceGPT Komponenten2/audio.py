import os
import wave
import pyaudio
import speech_recognition as sr
import datetime
import gc

def record_audio():
    try:
        now = datetime.datetime.now()
        output_folder = os.path.join(os.path.dirname(__file__), "output")
        os.makedirs(output_folder, exist_ok=True)
        output_filename = os.path.join(output_folder, f"output_{now.strftime('%Y-%m-%d_%H-%M-%S')}.wav")
        text_file = os.path.join(output_folder, f"output_{now.strftime('%Y-%m-%d_%H-%M-%S')}.txt")

        # Audioeinstellungen
        chunk = 1024  # Anzahl der Frames pro Datenblock
        sample_format = pyaudio.paInt16  # Sampleformat (16-Bit-Integer)
        channels = 1  # Anzahl der Audiokanäle (Mono: 1, Stereo: 2)
        sample_rate = 44100  # Abtastrate in Hz (Anzahl der Samples pro Sekunde)
        record_seconds = 10  # Aufnahmedauer in Sekunden


        # PyAudio-Objekt erstellen
        audio = pyaudio.PyAudio()

        # Stream öffnen
        stream = audio.open(format=sample_format,
                            channels=channels,
                            rate=sample_rate,
                            input=True,
                            frames_per_buffer=chunk)

        print("Aufnahme wird für 10 Sekunden gestartet...")

        # Aufnahme-Liste für die aufgezeichneten Frames
        frames = []

        # Aufnehmen der Audio-Daten
        for i in range(int(sample_rate / chunk * record_seconds)):
            data = stream.read(chunk)
            frames.append(data)

        print("Aufnahme beendet.")

        # Stream schließen
        stream.stop_stream()
        stream.close()
        audio.terminate()

        # Öffnen der Wave-Datei im Schreibmodus
        wave_file = wave.open(output_filename, 'wb')

        # Festlegen der Anzahl der Audiokanäle (Mono oder Stereo)
        wave_file.setnchannels(channels)

        # Festlegen der Samplebreite basierend auf dem Sampleformat
        wave_file.setsampwidth(audio.get_sample_size(sample_format))

        # Festlegen der Abtastrate (Anzahl der Samples pro Sekunde)
        wave_file.setframerate(sample_rate)

        # Schreiben der Audiodaten in die Datei
        wave_file.writeframes(b''.join(frames))

        # Schließen der Wave-Datei
        wave_file.close()

        # Ausgabe der gespeicherten Datei
        print("Audio-Datei gespeichert:", output_filename)

        # Rückgabe der gespeicherten Datei und einer Textdatei (falls vorhanden)
        return output_filename, text_file

    except OSError as e:
        if e.errno == -9996:
            # Spezielle Fehlermeldung für fehlendes Mikrofon anzeigen
            print("Fehler: Kein Mikrofon angeschlossen. Bitte ein Mikrofon anschließen und erneut versuchen.")
        else:
            # Allgemeine Fehlermeldung für andere OSError ausgeben
            print("Ein Fehler ist aufgetreten:", str(e))

        # Rückgabe von None-Werten, um auf den Fehler hinzuweisen
        return None, None


def transcribe_audio(output_filename, text_file):
    r = sr.Recognizer()  # Erstelle ein SpeechRecognizer-Objekt
    text = ""  # Initialisiere einen leeren String für den transkribierten Text

    try:
        with sr.AudioFile(output_filename) as source:  # Öffne die Audiodatei zum Lesen
            audio_data = r.record(source)  # Lese die Audiodaten
            detected_language = r.recognize_google(audio_data)  # Erkenne die Sprache der Audiodaten
            if detected_language:  # Wenn eine Sprache erkannt wurde
                detected_language = detected_language.encode('utf-8').decode('unicode_escape')  # Behandele die Codierung
                text = r.recognize_google(audio_data, language='de-DE')  # Transkribiere die Audiodaten auf Deutsch
                print("Erkannter Text:", text)  # Gib den transkribierten Text aus

    except sr.UnknownValueError:
        print("Keine Sprache erkannt.")
        os.remove(output_filename)
        print("Audiodatei gelöscht:", output_filename)
    except sr.RequestError as e:
        print("Fehler bei der Spracherkennung:", str(e))

    # Text nur speichern, wenn Sprache erkannt wurde
    if text:
        with open(text_file, 'w') as f:
            f.write(text)
        print("Text gespeichert:", text_file)
    else:
        # Wenn keine Sprache erkannt wurde, Textdatei löschen, falls vorhanden
        if os.path.exists(text_file):
            os.remove(text_file)
        print("Textdatei gelöscht:", text_file)
        text = "Keine Spracheingabe erkannt, bitte wiederholen!"  # Text für den Fall, dass keine Sprache erkannt wurde

    # Lösche den audio_data-Puffer, um Speicher freizugeben
    del audio_data
    gc.collect()

    return text

























