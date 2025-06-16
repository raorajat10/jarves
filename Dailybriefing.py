import pyttsx3
import speech_recognition
import os
import psutil
import datetime

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
def getweather():
    try: 
        city = "Jaipur"
        url= f"https://wttr.in/{city}?format=%t"
        weather = weather.request(url).text.strip()
        return f"The current weather in {city} is {weather}."
    except:
        return "Sorry Boss, I couldn't retrieve the weather information at this time."
    
def dailyBriefing():
    from systemMonitor import systemStatus
    systemStatus()
    
    now = datetime.datetime.now()
    speak(f"It is {now.strftime('%A, %B %d, %Y')}.")
    
    weather = getweather()
    speak(weather)
    
    if os.path.exists("focus.txt"):
        with open("focus.txt", "r") as file:
            lines = file.readlines()
            focus_sessions=len(lines)
        speak(f"You have {focus_sessions} focus sessions scheduled so far.")
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            tasks=[line.strip() for line in file if line.strip()]
        speak(f"You have {tasks} tasks scheduled for today.")
        
    from  systemMonitor import systemStatus,speak       
    systemStatus()