import pyttsx3
import datetime
import os

# engine = pyttsx3.init("sapi5")
# voices = engine.getProperty("voices")
# engine.setProperty("voice", voices[0].id)
# engine.setProperty("rate", 190)

# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()
from brianTTS import speak
extractedTme=open("Alarmtext.txt","rt") 
time=extractedTme.read() 
Time=str(time)
extractedTme.close() 

deleteTime=open("Alarmtext.txt","r+")
deleteTime.truncate(0)
deleteTime.close()


def ringAlarm():
    timeSet=str(time)
    timenow=timeSet.replace("friday ","")
    timenow=timeSet.replace("set an alarm ","")
    timenow=timeSet.replace("alarm ","")
    timenow=timeSet.replace("set alarm ","")
    timenow=timeSet.replace(" and ",":")
    AlarmTime = str(timenow)
    print(AlarmTime)
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        if current_time == AlarmTime:
            speak("Alarm ringing")
            os.startfile("Alarm.mp3")
        elif current_time + "00:00:30" == AlarmTime:
            exit()
              
ringAlarm(time)    
    
    