from groq import Groq

client = Groq(api_key="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")
command = input('''Enter your command: 
[20/07/26, 10:06:00 AM] cccc: Tor laptop lagbe na tui to rog ghor asbi problem hoba nae
[20/07/26, 10:06:02 AM] Anirban2.0: Nahh samnei
[20/07/26, 10:06:06 AM] Anirban2.0: Jata at korbo
[20/07/26, 10:06:15 AM] Anirban2.0: Bagnan er 2 to station porei
[20/07/26, 10:06:44 AM] গৌ🙂র😊ব😁: Tha hole laptop akhon lagbe nae 
Tor ma koba ja toka dura pathabe 😴 ''')

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful AI assistant."
        },
        {
            "role": "user",
            "content": command
        }
    ],
    model="llama-3.3-70b-versatile"
)

print(chat_completion.choices[0].message.content)
