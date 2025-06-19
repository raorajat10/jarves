import pyttsx3
import speech_recognition
import os
import psutil
import datetime
import requests

# === Text-to-Speech Setup ===
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 190)

def speak(audio):
    print("JARVIS:", audio)
    engine.say(audio)
    engine.runAndWait()

# === Speech Recognition ===
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
        except Exception:
            print("Sorry Boss, I didn't get that. Please repeat.")
            return "None"
    return query

# === Weather Fetcher ===
def getWeather():
    try: 
        city = "Jaipur"
        url = f"https://wttr.in/{city}?format=%t"
        weather = requests.get(url).text.strip()
        return f"The current weather in {city} is {weather}."
    except:
        return "Sorry Boss, I couldn't retrieve the weather information at this time."

# === System Status ===
def systemStatus():
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    battery = psutil.sensors_battery()
    battery_percent = battery.percent if battery else "Unknown"
    speak(f"System check: CPU {cpu}%, RAM {ram}%, Battery {battery_percent}%.")

# === Daily Briefing ===
def dailyBriefing():
    systemStatus()

    now = datetime.datetime.now()
    speak(f"It is {now.strftime('%A, %B %d, %Y')}.")

    weather = getWeather()
    speak(weather)

    if os.path.exists("focus.txt"):
        with open("focus.txt", "r") as file:
            lines = file.readlines()
        focus_sessions = len(lines)
        speak(f"You have completed {focus_sessions} focus sessions.")

    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            tasks = [line.strip() for line in file if line.strip()]
        speak(f"You have {len(tasks)} tasks scheduled for today.")
