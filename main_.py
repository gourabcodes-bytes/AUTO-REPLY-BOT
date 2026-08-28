import os
import re
import pyautogui
import pyperclip
import time
import groq
from groq import Groq

client = Groq(api_key="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")



def is_last_message_from_sender(chat_history):
    pattern = r"\[(.*?)\]\s([^:]+):"
    matches= re.findall(pattern,chat_history)
    print(is_last_message_from_sender(copied_text))
    if not matches:
        print("Debug: No chat pattern matched.")
        return False
    last_sender = matches[-1][1].strip()
    print("Last sender:", last_sender)  # Debug
    return last_sender.lower() == "monti dae"
print("Switch to your chat window now...")

        

    


   

   
    # Give yourself time to switch to the target window
time.sleep(3)


    # -----------------------------
    # Step 1: Click on the icon
    # -----------------------------
pyautogui.click(1049, 87)
    # Wait for the UI to respond
time.sleep(1)




    # -----------------------------
    # Step 2: Drag to select the text
    # -----------------------------
pyautogui.moveTo(1049, 87, duration=0.3)
pyautogui.dragTo(1399,578,duration=1,button="left")

# Wait a moment
time.sleep(0.5)

# -----------------------------
# Step 3: Copy selected text
# -----------------------------
pyautogui.hotkey("command", "c")   # macOS

# For Windows/Linux use:
# pyautogui.hotkey("ctrl", "c")

time.sleep(0.5)

# -----------------------------
# Step 4: Read clipboard
# -----------------------------
copied_text = pyperclip.paste()

print("Copied text:")
print(repr(copied_text))


# Now the text is stored in this variable
print("----------")

# print("\nVariable contents:")
# print(text)
# print(is_last_message_from_sender(copied_text))
if is_last_message_from_sender(copied_text):
    print("Condition met! Calling Groq API....")
    try:

        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": '''You are Gourab.
                                Reply naturally like a real human.
                                Keep replies short.
                                Use Bengali and English naturally.
                                Don't sound like an AI.'''
                },
                {
                    "role": "user",
                    "content": copied_text
                    
                }
            ],
            model="llama-3.3-70b-versatile"
        )

        responce = chat_completion.choices[0].message.content
        pyperclip.copy(responce)
        pyautogui.click(1315, 600)
        time.sleep(1)

        # Copy the text to the clipboard


        # Paste it
        # Windows/Linux:
        pyautogui.hotkey("command", "v")
        time.sleep(1)
        # macOS: use pyautogui.hotkey("command", "v")

        # Press Enter
        pyautogui.press("enter")
        print("Message sent successfully.")
    except Exception as e:
        print(f"An error occurred during API execution: {e}")
else:
    print("Script finished: The last message was not from Monti dae.")