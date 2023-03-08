import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

l = ["Rahul", "Nishant", "Harry", "Aniket", "Neeraj", "Sourav"]

for names in l:
    speaker.Speak(f"Shoutout to {names}")

