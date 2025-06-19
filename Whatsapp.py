import pywhatkit
import pyttsx3
import datetime
import speech_recognition
import webbrowser
from bs4 import BeautifulSoup
from time import sleep
from datetime import datetime
from datetime import timedelta
import os

# Initialize TTS engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 190)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function to take voice command
def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 500
        audio = r.listen(source, 0, 4)

        try:
            print("Understanding...")
            query = r.recognize_google(audio, language="en-in")
            print(f"You said: {query}\n")
        except Exception as e:
            print("Sorry Boss, I didn't get that. Please repeat.")
            return "None"
    return query 
strTime=int(datetime.now().strftime("%H"))
update = int((datetime.now()+timedelta(minutes=2)).strftime("%M"))
def SendMessage():
    speak("Please tell me the name of the person you want to send a message to.")   
    a = int(input('''Person 1-1
            Person 2-2
            Person 3-3
            '''))
    if a==1:
        speak("Please tell me the message you want to send.")
        message=str(input("enter the message"))
        pywhatkit.sendwhatmsg("+919782740000",message,time_hour=strTime,time_min=update)
    elif a==2:
        pass    
        
    