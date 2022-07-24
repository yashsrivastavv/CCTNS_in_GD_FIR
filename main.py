import sys
import pyttsx3
import speech_recognition as sr
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)


def takeInput():
    """Take User input through microphone & returns string output """
    count = 0
    while count == 0:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User Said: {query}\n")
            count += 1
        except Exception:
            print("Say That Again Please...")
            return 'None'
        return query


while True:
    say = takeInput().lower()
    if 'exit' in say:
        sys.exit()
