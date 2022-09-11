import sys
import pyttsx3
import speech_recognition as sr
import datetime
import pandas as pd
import numpy as np
import time
import dask.dataframe as dd
engine = pyttsx3.init('dummy')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)
global query


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
        # key_to_search = query

        start = time.time()
        dtypes = {

            "RKY": "object",
            "LOCAT": "str",
            "ACTION": "str",
            "TRUCK": "str",
            "BUS": "str",
            "FID": "uint8"

        }
        data = dd.read_csv('traffic_crashes.csv', delimiter=",")
        end = time.time()
        print(end - start, 'sec')
        var = query.upper()
        print(data[data['LOCAT'] == var].head())
        print(var)
        exit()

        '''Error: breaks the code after one query without executing the searching algorithm'''
    except Exception as e:
        print("Say That Again Please...")
        return 'None'
    return query



while True:
    say = takeInput().lower()

