###Voice-GPT
##Voice-GPT ist ein Projekt, das die OpenAI GPT-3-Technologie verwendet, um Sprachaufnahmen zu transkribieren und Fragen basierend auf dem transkribierten Text zu beantworten.

##Funktionen:

Aufnahme von Sprachaudios: Die Anwendung ermöglicht es Benutzern, Sprachaufnahmen zu machen.
Transkription von Audios: Die aufgenommenen Sprachaudios werden automatisch transkribiert und der Text wird extrahiert.
Frage-Antwort-Service: Basierend auf dem transkribierten Text kann der Benutzer Fragen stellen und die Anwendung generiert eine Antwort mithilfe der OpenAI GPT-3-Technologie.
Datenbankintegration: Die Anwendung speichert die aufgenommenen Audios und die dazugehörigen transkribierten Texte in einer SQLite-Datenbank.
Garbage Collector: Die Anwendung enthält einen Garbage Collector, der regelmäßig ältere Audiodateien und Textdateien aus dem Speicher löscht.

##Anleitung zur Verwendung:

Klonen Sie das Repository auf Ihren lokalen Computer.
Stellen Sie sicher, dass Python und die erforderlichen Abhängigkeiten installiert sind. Verwenden Sie dazu den Befehl pip install -r requirements.txt.
Starten Sie die Anwendung, indem Sie den Befehl python main.py ausführen.
Öffnen Sie einen Webbrowser und navigieren Sie zur URL http://127.0.0.1:5000.
Nehmen Sie eine Sprachaufnahme auf, indem Sie auf den entsprechenden Button klicken.
Die Anwendung transkribiert automatisch das aufgenommene Audio und zeigt den transkribierten Text an.
Geben Sie eine Frage in das Textfeld ein und klicken Sie auf "Frage stellen". Die Anwendung generiert eine Antwort basierend auf dem transkribierten Text und zeigt sie an.

##Anforderungen:

Python 3.x
Flask
PyAudio
SpeechRecognition
OpenAI Python
Stellen Sie sicher, dass Sie die erforderlichen API-Schlüssel für die OpenAI GPT-3-Technologie haben und fügen Sie sie in der Datei api_service.py ein, um die Frage-Antwort-Funktion nutzen zu können.

##Autor
[Christian Schröder & Alexander Ibach]

Lizenz
Dieses Projekt ist unter der MIT-Lizenz lizenziert.

## Bilder

In diesem Projekt werden Bilder verwendet, um das visuelle Design zu unterstützen. Aufgrund der Dateigrößenbeschränkung des Repositories können die Bilder nicht direkt hier abgelegt werden. Sie müssen die Bilder manuell herunterladen und in den entsprechenden Ordnern platzieren, um das Projekt korrekt auszuführen.

### Platzierung der Bilder

Folgende Bilder werden verwendet:

- Hintergrundvideo: Das Hintergrundvideo wird im HTML-Code referenziert. Um das Video anzuzeigen, platzieren Sie es im Ordner "static" und aktualisieren Sie den Dateipfad im HTML-Code.

### Aktualisierung des HTML-Codes

In der HTML-Datei (`index.html`) finden Sie die entsprechenden Stellen, an denen die Bilder referenziert werden. Passen Sie die Dateipfade entsprechend an, um sicherzustellen, dass die Bilder korrekt angezeigt werden.

Bitte beachten Sie, dass die Ordnerstruktur und die Dateinamen beibehalten werden sollten, um die Konsistenz des Projekts zu gewährleisten.


Hinweise
Dieses Projekt wurde im Rahmen eines Abschlussprojekts erstellt. Bitte beachten Sie, dass die OpenAI GPT-3-Technologie kostenpflichtig ist und die Nutzung der API-Schlüssel zu Kosten führen kann.

Wenn Sie Fragen oder Probleme mit dem Projekt haben, kontaktieren Sie mich bitte unter [ibachalex13@gmail.com].

Vielen Dank für Ihr Interesse an Voice-GPT!
Chris & Alex
