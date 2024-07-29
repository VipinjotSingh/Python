import speech_recognition as sr
import os
import openai
import pyttsx3 as pt
from config import apikey
import pyaudio as pa
import pyttsx3 as pts
import webbrowser as wb
import datetime as dt

import openai
from config import apikey
openai.api_key = apikey


speaker = pt.init()
speaker.setProperty('rate', 165)  # Set the speech rate
speaker.setProperty('volume', 1.0)

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.5
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-us")
            print(f"{query}")
            return query
        except Exception as e:
            print("Say that again please...")
            return "None"

def speak(text):
    speaker.say(text)
    speaker.runAndWait()

speak("Hello I am Jarvis A.I")

def conversational_mode():
    speak("How are you today?")
    response = takecommand()
    if "good" in response or "fine" in response:
        speak("That's great to hear! How can I help you today?")
    elif "feeling sad" in response or "not good" in response:
        speak("Sorry to hear that. Is there anything I can do to help you feel better?")
    else:
        speak("I didn't quite understand that. Can you please try again?")
        
            
#def open_spotify():
    #os.system('start spotify')

#open_spotify()
    

while True:
    conversational_mode()
    print("listening...")
    query = takecommand()
    speak("you said " + query)
    sites = [["Youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"],
             ["google", "https://www.google.com"], ["facebook", "https://www.facebook.com"], ["Gemini", "https://gemini.google.com/app"]]

    for site in sites:
        if f"open {site[0]}".lower() in query.lower():
            speak(f"wait opening {site[0]}")
            wb.open(site[1]) 
    

    if "whats the time" in query:
        strfTime = dt.datetime.now().strftime("%H:%M:%S")
        speak(f"the time is {strfTime}")
        
        
    if  "open spotify" in query:
        os.system('start spotify')
        speak(f"opening spotify")
    
    if "open camera" in query:
            if os.name == 'nt':
                speak(f"opening camera")
                os.system('start microsoft.windows.camera:')
    
    if "open Google Chrome" in query:
            if os.name == 'nt':
                speak(f"opening Google Chrome, what should search for?")
                os.system('start microsoft.windows.Chrome:')   
                search_query = takecommand()
                speak(f"searching for {search_query}")
                wb.open(f"https://www.google.com/search?q={search_query}")

        