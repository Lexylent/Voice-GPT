import os
import signal
import socket
import logging



def cleanup_log_file(log_file_path, max_size_mb=1, max_entries=10):
    """
    Überprüft die Größe und Anzahl der Einträge in einer Log-Datei und räumt sie auf, falls die Kriterien überschritten werden.

    Args:
        log_file_path (str): Der Pfad zur Log-Datei.
        max_size_mb (int): Die maximale Größe der Log-Datei in Megabyte. Standardmäßig auf 1 MB gesetzt.
        max_entries (int): Die maximale Anzahl von Einträgen in der Log-Datei. Standardmäßig auf 10 Einträge gesetzt.
    """
    if os.path.isfile(log_file_path):
        file_size = os.path.getsize(log_file_path) / (1024 * 1024)  # Umrechnung in Megabyte
        if file_size > max_size_mb:
            os.remove(log_file_path)
            print("Log-Datei aufgrund der Größe aufgeräumt.")
            return

        with open(log_file_path, 'r') as file:
            lines = file.readlines()
            if len(lines) > max_entries:
                with open(log_file_path, 'w') as file:
                    file.writelines(lines[-max_entries:])
                print("Log-Datei aufgrund der Anzahl der Einträge aufgeräumt.")
    else:
        print("Log-Datei nicht gefunden.")






# Logging-Konfiguration
logging.basicConfig(filename='server.log', level=logging.INFO)

def check_port_in_use(port):
    """
    Überprüft, ob ein bestimmter Port auf dem lokalen Rechner verwendet wird.

    Args:
        port (int): Die Portnummer, die überprüft werden soll.

    Returns:
        bool: True, wenn der Port verwendet wird, False sonst.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0

def stop_previous_instance(port):
    """
    Beendet eine zuvor gestartete Instanz eines Servers auf dem angegebenen Port.

    Falls ein Server auf dem angegebenen Port läuft, versucht diese Funktion ihn zu beenden, indem sie die Prozess-ID (PID)
    aus der Datei 'server.pid' liest, ein Terminationssignal (SIGTERM) an den Prozess sendet und die Datei 'server.pid' entfernt.

    Args:
        port (int): Die Portnummer, auf der der Server läuft.

    Raises:
        FileNotFoundError: Wenn die Datei 'server.pid' nicht gefunden wird.
        ProcessLookupError: Wenn ein Fehler beim Beenden des Prozesses auftritt.
    """
    if check_port_in_use(port):
        try:
            with open('server.pid', 'r') as file:
                pid = int(file.read().strip())
                os.kill(pid, signal.SIGTERM)
            os.remove('server.pid')
            logging.info("Vorherige Instanz wurde erfolgreich beendet.")
        except FileNotFoundError:
            logging.warning("Die Datei 'server.pid' wurde nicht gefunden.")
        except ProcessLookupError:
            logging.error("Fehler beim Beenden des vorherigen Serverprozesses.")
        except OSError as e:
            logging.error("Fehler beim Beenden des vorherigen Serverprozesses: %s", str(e))
    else:
        logging.warning("Keine vorherige Instanz gefunden.")

def start_new_instance(port):
    """
    Startet eine neue Instanz eines Servers auf dem angegebenen Port.

    Diese Funktion schreibt die aktuelle Prozess-ID (PID) in die Datei 'server.pid'.

    Args:
        port (int): Die Portnummer, auf der der Server laufen soll.
    """
    try:
        if not check_port_in_use(port):
            with open('server.pid', 'w') as file:
                file.write(str(os.getpid()))
    except OSError as e:
        logging.error("Fehler beim Schreiben der PID-Datei: %s", str(e))

def main():
    port = 5000

    # Überprüfen, ob der Port bereits verwendet wird
    is_port_in_use = check_port_in_use(port)

    if is_port_in_use:
        # Vorherige Instanz beenden
        stop_previous_instance(port)
    else:
        # Keine vorherige Instanz gefunden
        logging.info("Keine vorherige Instanz gefunden.")

    # Neue Instanz starten, wenn der Port nicht bereits verwendet wird
    if not is_port_in_use:
        start_new_instance(port)

    #Bereinigt die Log-Datei, indem alte Einträge entfernt werden, wenn sie eine bestimmte Größe oder Anzahl überschreiten
    cleanup_log_file('server.log', max_size_mb=1, max_entries=10)
    ''' Args:
        log_file (str): Der Name der Log-Datei.
        max_size_mb (int): Die maximale Größe der Log-Datei in Megabytes.
        max_entries (int): Die maximale Anzahl von Einträgen in der Log-Datei.

    Returns:
        None
    '''


if __name__ == "__main__":
    # Logging-Konfiguration
    logging.basicConfig(filename='server.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    main()
