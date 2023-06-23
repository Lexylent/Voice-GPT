import openai

openai.api_key ='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' #CHATGPT KEY

# Versuche, eine Anfrage an OpenAI zu stellen
def generate_answer(question):
    try:
        # Der Text, der den Generator informiert, dass es sich um eine Korrekturaufgabe handelt
        prompt = f"Frage: {question}\nAntwort:"

        # Die maximale Anzahl von Tokens (Texteinheiten) für die generierte Antwort
        max_tokens = 200

        # Aufruf der OpenAI API, um eine Textgenerierung durchzuführen
        response = openai.Completion.create(
            engine="text-davinci-003",  # Die gewählte Textgenerierungs-Engine
            prompt=prompt,  # Der vorbereitete Text, der den Generator instruiert
            max_tokens=max_tokens,  # Die maximale Länge der generierten Antwort
            n=1,  # Anzahl der gewünschten generierten Antworten (in diesem Fall nur eine)
            stop="Antwort",  # Es wird kein spezielles Stopp-Token verwendet, um das Ende der Antwort anzugeben
            temperature=0.5,  # Ein Maß für die Zufälligkeit der generierten Antwort
            top_p=1.0,  # Anteil der Wahrscheinlichkeiten der nächsten Token, die berücksichtigt werden sollen
            frequency_penalty=0.0,  # Strafe für die Verwendung bereits verwendeter Tokens basierend auf ihrer Häufigkeit
            presence_penalty=0.0  # Strafe für die Verwendung bereits verwendeter Tokens basierend auf ihrer Anwesenheit
        )
        
        # Überprüfe, ob eine Antwort vorhanden ist  
        if 'choices' in response and len(response['choices']) > 0:
            # Extrahiere den Text der ersten Antwort und entferne Leerzeichen am Anfang und Ende
            return response['choices'][0]['text'].strip()
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








