# Voice-GPT
## Voice-GPT ist ein Projekt, das die Python Technologie verwendet, um Sprachaufnahmen zu transkribieren und Fragen basierend auf dem transkribierten Text von der OpenAI API beantworten zu lassen.

## Funktionen:

1. Aufnahme von Sprachaudios: Die Anwendung ermöglicht es Benutzern, Sprachaufnahmen zu machen.
2. Transkription von Audios: Die aufgenommenen Sprachaudios werden automatisch transkribiert und der Text wird extrahiert.
3. Frage-Antwort-Service: Basierend auf dem transkribierten Text kann der Benutzer Fragen stellen und die Anwendung generiert eine Antwort mithilfe der OpenAI GPT-3-Technologie.
4. Datenbankintegration: Die Anwendung speichert die aufgenommenen Audios und die dazugehörigen transkribierten Texte in einer SQLite-Datenbank.
5. Garbage Collector: Die Anwendung enthält einen Garbage Collector, der regelmäßig ältere Audiodateien und Textdateien aus dem Speicher löscht.

## Anleitung zur Verwendung:

1. Klonen Sie das Repository auf Ihren lokalen Computer.
2. Stellen Sie sicher, dass Python und die erforderlichen Abhängigkeiten installiert sind. Verwenden Sie dazu den Befehl `pip install -r requirements.txt`.
3. Starten Sie die Anwendung, indem Sie den Befehl `python main.py` ausführen.
4. Öffnen Sie einen Webbrowser und navigieren Sie zur URL `http://127.0.0.1:5000`.
5. Nehmen Sie eine Sprachaufnahme auf, indem Sie auf den entsprechenden Button klicken.
6. Die Anwendung transkribiert automatisch das aufgenommene Audio und zeigt den transkribierten Text an.
7. Überprüfen Sie den transkribierten Text und korrigieren Sie ihn gegebenenfalls, falls erforderlich.
8. Sende sie den Text ab in dem sie auf "Absenden" drücken.
### Hinweis: Der Text, der aus dem Audio in Text umgewandelt wird, steht bereits zum Absenden bereit in der unteren Zeile, in der Sie den Text eventuell noch vor dem Absenden korrigieren können, wenn nötig.


## Unit Tests

Dieses Projekt enthält Unit-Tests, um die Funktionalität der Anwendung zu überprüfen. Die Unit-Tests werden mithilfe des Python-Test-Frameworks `unittest` ausgeführt.

## Beschreibung der Tests

Die `unittest_app.py` Datei enthält die Definition der Unit-Tests. Hier ist eine Beschreibung der enthaltenen Tests:

- `test_index_route`: Überprüft den Aufruf der Indexroute `'/'` und den Statuscode der Antwort.
- `test_transcribe_route`: Überprüft den Aufruf der Transcribe-Route `'/transcribe'` und den Statuscode sowie den Content-Type der Antwort.
- `test_correct_route`: Überprüft den Aufruf der Correct-Route `'/correct'` mit JSON-Daten, den Statuscode, den Content-Type und die enthaltenen JSON-Daten der Antwort.

Die Testfälle verwenden die Assertions von `unittest`, um die erwarteten Ergebnisse zu überprüfen.

Stellen Sie sicher, dass Sie die erforderlichen Abhängigkeiten und die richtige Umgebung eingerichtet haben, um die Tests erfolgreich auszuführen.


### Ausführen der Tests

Um die Tests auszuführen, stellen Sie sicher, dass Sie die erforderlichen Abhängigkeiten installiert haben und folgen Sie den nachstehenden Schritten:

1. Navigieren Sie zum Wurzelverzeichnis des Projekts.
2. Öffnen Sie ein Terminal oder eine Befehlszeile.
3. Geben Sie den folgenden Befehl ein, um die Tests auszuführen:

python -m unittest utittest_app.py

## Anforderungen:

1. Python 3.x
2. Flask
3. PyAudio
4. SpeechRecognition
5. OpenAI Python

## Zusammenfassung der audio.py-Funktionalität:

### Die audio.py-Datei in diesem Repository stellt Funktionen zur Aufnahme von Audio und zur Transkription von Sprache in Text bereit.

Die record_audio()-Funktion ermöglicht die Aufnahme von Audio mithilfe des PyAudio-Moduls. Sie definiert die Audioeinstellungen wie Chunkgröße, Sampleformat, Anzahl der Kanäle und Abtastrate. Die Aufnahme dauert eine bestimmte Zeit und die aufgezeichneten Frames werden in einer Liste gespeichert. Anschließend wird das aufgenommene Audio in einer Wave-Datei gespeichert.

Die transcribe_audio(output_filename, text_file)-Funktion verwendet das SpeechRecognition-Modul, um das aufgenommene Audio zu transkribieren. Sie öffnet die Wave-Datei zum Lesen, liest die Audiodaten und erkennt die Sprache des Audios. Falls eine Sprache erkannt wird, wird das Audio in Text transkribiert und der transkribierte Text wird ausgegeben. Der transkribierte Text wird auch in einer Textdatei gespeichert.

Die audio.py-Datei bietet Fehlerbehandlung für verschiedene Szenarien, wie das Fehlen eines Mikrofons oder Fehler bei der Spracherkennung. Sie enthält auch Funktionen zur Bereinigung des Speichers, um Ressourcen freizugeben.

Diese Funktionalität ermöglicht es Benutzern, Spracheingaben aufzuzeichnen und in Text umzuwandeln, was nützlich sein kann, um Audioinhalte zu transkribieren oder Sprachbefehle zu verarbeiten.

Hinweis: Die Verwendung der audio.py-Funktionen erfordert die Installation der erforderlichen Python-Module wie PyAudio und SpeechRecognition.
   
### Stellen Sie sicher, dass Sie die erforderlichen API-Schlüssel für die OpenAI GPT-3-Technologie haben und fügen Sie sie in der Datei api_service.py ein, um die Frage-Antwort-Funktion nutzen zu können.

## Bilder

In diesem Projekt werden Bilder verwendet, um das visuelle Design zu unterstützen. Aufgrund der Dateigrößenbeschränkung des Repositories können die Bilder nicht direkt hier abgelegt werden. Sie müssen die Bilder manuell einfügen (sie können eigene bilder als Hintergrund verwenden) und in den entsprechenden Ordnern platzieren, um das Projekt korrekt auszuführen.

### Platzierung der Bilder

Folgende Bilder werden verwendet:

- Hintergrundvideo: Das Hintergrundvideo wird im HTML-Code referenziert. Um das Video anzuzeigen, platzieren Sie es im Ordner "static" und aktualisieren Sie den Dateipfad im HTML-Code.

### Aktualisierung des HTML-Codes

In der HTML-Datei (`index.html`) finden Sie die entsprechenden Stellen, an denen die Bilder referenziert werden. Passen Sie die Dateipfade entsprechend an, um sicherzustellen, dass die Bilder korrekt angezeigt werden.

Bitte beachten Sie, dass die Ordnerstruktur und die Dateinamen beibehalten werden sollten, um die Konsistenz des Projekts zu gewährleisten.


## Hinweise
Dieses Projekt wurde im Rahmen eines Abschlussprojekts erstellt. Bitte beachten Sie, dass die OpenAI GPT-3-Technologie kostenpflichtig ist und die Nutzung der API-Schlüssel zu Kosten führen kann.

## Autor
### Christian Schröder & Alexander Ibach

Lizenz
Dieses Projekt ist unter der MIT-Lizenz lizenziert.

Wenn Sie Fragen oder Probleme mit dem Projekt haben, kontaktieren Sie mich bitte ### Nicht! ;))

Vielen Dank für Ihr Interesse an Voice-GPT!
Chris & Alex
