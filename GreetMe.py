import pyttsx3
import datetime

# Initialize TTS engine

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 190)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    hour = int(datetime.datetime.now().hour)

    # Determine the appropriate greeting based on the time of day
    if hour >= 0 and hour < 12:
        speak("Good morning Boss!")
        from Dailybriefing import dailyBriefing
        dailyBriefing()
    elif hour >= 12 and hour < 18:
        speak("Good afternoon Boss!")
        from Dailybriefing import dailyBriefing
        dailyBriefing()
    else:
        speak("Good evening Boss !")
        from Dailybriefing import dailyBriefing
        dailyBriefing()
        
        