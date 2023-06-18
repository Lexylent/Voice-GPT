import os
import glob
import time
import threading

def garbage_collector():
    while True:
        files = glob.glob('output/*')  # Liste aller Dateien im output-Ordner
        if len(files) > 1:  # Prüfen, ob mehr als eine Datei vorhanden ist (mind. eine WAV-Datei und eine TXT-Datei)
            files.sort(key=os.path.getmtime)  # Sortieren der Dateien nach dem Änderungszeitpunkt (älteste zuerst)
            oldest_wav = files[0]  # Älteste WAV-Datei
            oldest_txt = files[1]  # Älteste TXT-Datei
            os.remove(oldest_wav)  # Löschen der ältesten WAV-Datei
            os.remove(oldest_txt)  # Löschen der ältesten TXT-Datei
            print("Audio-Datei gelöscht:", oldest_wav)
            print("Text-Datei gelöscht:", oldest_txt)
        time.sleep(8 * 60 * 60)  # Warte 8 Stunden

def start_garbage_collector():
    garbage_thread = threading.Thread(target=garbage_collector)
    garbage_thread.start()

