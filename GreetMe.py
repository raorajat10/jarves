import pyttsx3
import datetime

# Initialize TTS engine

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    hour = int(datetime.datetime.now().hour)

    # Determine the appropriate greeting based on the time of day
    if hour >= 0 and hour < 12:
        speak("Good morning Boss! How can I assist you today?")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon Boss! How can I assist you today?")
    else:
        speak("Good evening Boss ! How can I assist you today?")
        
        speak("I am your personal assistant. I am here to help you with your tasks.")