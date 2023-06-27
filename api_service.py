import openai
import json

openai.api_key = 'Hier_kommt_der_apikey_hinein'  # CHATGPT KEY

# Vorheriger Konversationsverlauf
previous_conversation = []

# Versuche, eine Anfrage an OpenAI zu stellen
def generate_answer(question):
    global previous_conversation  # Deklariere die Variable als global

    try:
        # Aufbau des Konversationsverlaufs
        conversation = previous_conversation.copy()
        conversation.append(question)   # Benutzereintrag mit der gestellten Frage

        # Die maximale Anzahl von Tokens (Texteinheiten) für die generierte Antwort
        max_tokens = 400
        

        # Konvertiere den Konversationsverlauf in einen JSON-String
        prompt = json.dumps(conversation)

        # Aufruf der OpenAI API, um eine Textgenerierung durchzuführen
        response = openai.Completion.create(
            engine="text-davinci-003",  # Die gewählte Textgenerierungs-Engine
            prompt=prompt,  # Der Konversationsverlauf als Prompt
            max_tokens=max_tokens,  # Die maximale Länge der generierten Antwort
            n=1,  # Anzahl der gewünschten generierten Antworten (in diesem Fall nur eine)
            temperature=0.8,  # Ein Maß für die Zufälligkeit der generierten Antwort
            top_p=1.0,  # Anteil der Wahrscheinlichkeiten der nächsten Token, die berücksichtigt werden sollen
            frequency_penalty=0.0,  # Strafe für die Verwendung bereits verwendeter Tokens basierend auf ihrer Häufigkeit
            presence_penalty=0.0  # Strafe für die Verwendung bereits verwendeter Tokens basierend auf ihrer Anwesenheit
        )

        # Überprüfe, ob eine Antwort vorhanden ist
        if 'choices' in response and len(response['choices']) > 0:
            # Extrahiere den Text der ersten Antwort und entferne Leerzeichen am Anfang und Ende
            answer = response['choices'][0]['text'].strip()
            answer_text = answer.split('{"role": "assistant", "content": ')[-1].strip('"}')

            print(answer_text)

            # Konversationsverlauf aktualisieren
            conversation.append({"role": "assistant", "content": answer_text})
            previous_conversation = conversation  # Speichern des aktualisierten Konversationsverlaufs

            return answer_text




        else:
            # Falls keine Antwort gefunden wurde, gib einen entsprechenden Text zurück
            return 'Keine Antwort gefunden.'

    except openai.OpenAIError as e:
        # Fehlerbehandlung für OpenAI-Fehler
        print("OpenAI Error:", str(e))
        return 'Fehler bei der Kommunikation mit der OpenAI API.'

    except Exception as e:
        # Allgemeine Fehlerbehandlung
        print("Ein Fehler ist aufgetreten:", str(e))
        return 'Ein unerwarteter Fehler ist aufgetreten.'
