import sqlite3

DATABASE_NAME = 'database.db'  # Name der Datenbankdatei

def create_tables():
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()

    # Erstelle die Tabellen, falls sie noch nicht existieren
    c.execute('''CREATE TABLE IF NOT EXISTS user (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    email TEXT
                 )''')

    c.execute('''CREATE TABLE IF NOT EXISTS recordings (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    audio_filename TEXT,
                    text_filename TEXT
                 )''')

    conn.commit()
    conn.close()

def insert_user(name, email):
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()

    c.execute("INSERT INTO user (name, email) VALUES (?, ?)", (name, email))

    conn.commit()
    conn.close()

def insert_recording(audio_filename, text_filename):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    # Füge die Aufnahme in die Datenbank ein
    query = "INSERT INTO recordings (audio_filename, text_filename) VALUES (?, ?)"
    cursor.execute(query, (audio_filename, text_filename))

    # Übernehme die Änderungen und schließe die Verbindung
    conn.commit()
    conn.close()