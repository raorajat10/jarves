
import pyttsx3
import speech_recognition
import os
import psutil

# engine = pyttsx3.init("sapi5")
# voices = engine.getProperty("voices")
# engine.setProperty("voice", voices[0].id)
# engine.setProperty("rate", 190)

# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()
from brianTTS import speak
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

def systemStatus():
    cpu=psutil.cpu_percent()
    ram=psutil.virtual_memory().percent
    battery=psutil.sensors_battery()
    battery_percent = battery.percent if battery else "No battery info"
    
    speak(f"CPU usage is at {cpu} percent, RAM usage is at {ram} percent, and battery level is at {battery_percent} percent.")
    speak("How can I assist you today?")