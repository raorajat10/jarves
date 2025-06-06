from time import sleep
import time
from googletrans import Translator
import googletrans
from gtts import gTTS
import os
import speech_recognition 
import pyttsx3
from playsound import playsound


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

def translate_text(query):
    speak("sure Boss, I will translate it for you")
    print(googletrans.LANGUAGES)
    translator = Translator()
    speak("Choose the language you want to translate to")
    b = input("To language: ")
    text_to_translate = translator.translate(query,src="auto", dest=b)
    text = text_to_translate.text
    
    try:
        speakg1= gTTS(text=text, lang=b, slow=False)
        speakg1.save("translated.mp3")
        playsound("translated.mp3")
        
        
        time.sleep(5)
        os.remove("translated.mp3")
    except:
        print("Error in translation or playback.")
        speak("Sorry Boss, I couldn't translate that.")    