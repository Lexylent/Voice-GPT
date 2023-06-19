import openai

openai.api_key ='Hier_kommt_der-apikey_hinein' #CHATGPT KEY

# Versuche, eine Anfrage an OpenAI zu stellen
def generate_answer(question):
    try:
        prompt = f"Frage: {question}\nAntwort:"
        max_tokens = 100

        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=max_tokens,
            n=1,
            stop="Antwort:",
            temperature=0.5,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        # Überprüfe, ob eine Antwort vorhanden ist  
        if 'choices' in response and len(response['choices']) > 0:
            # Extrahiere den Text der ersten Antwort und entferne Leerzeichen am Anfang und End
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









