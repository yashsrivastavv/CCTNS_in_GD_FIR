import sys
import pyttsx3
import speech_recognition as sr
import datetime

engine = pyttsx3.init('dummy')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)



def takeInput():
    """Take User input through microphone & returns string output """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User Said: {query}\n")
        exit()
    except Exception as e:
        print("Say That Again Please...")
        return 'None'
    return query


def work():
    while True:
        say = takeInput().lower()

