import os
import pyautogui
import webbrowser
import pyttsx3
from time import sleep

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 190)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

dictapp={"commandprompt:" : "cmd",
          "notepad": "notepad",
          "calculator": "calc",
          "msword": "winword",
          "excel": "excel",
          "powerpoint": "powerpnt",
          "paint": "mspaint",
          "chrome": "chrome",
          "firefox": "firefox",
          "safari": "safari",
          "explorer": "explorer",
          "edge": "msedge",
          "vlc": "vlc",
          "spotify": "spotify",
          "steam": "steam",
          }    
def openWebApp(query):
    speak("Opening the application Boss")
    if ".com" in query or ".in" in query or ".org" in query or ".net" in query:
        query = query.replace("open", "")
        query = query.replace("friday", "")
        query = query.replace("open with", "")
        query = query.replace("open with google", "")
        query = query.replace("launch", "")
        query = query.replace("launch with", "")
        query = query.replace("launch with google", "")
        query = query.replace(" ", "")
        webbrowser.open(f"https://www.{query}")
    else:
        keys= list(dictapp.keys())
        for app in keys:
            if app in query:
                # app = app.replace("open", "")
                # app = app.replace("friday", "")
                # app = app.replace("open with", "")
                # app = app.replace("launch", "")
                # app = app.replace("launch with", "")
                # app = app.replace(" ", "")
                os.system( f"start {dictapp[app]}")
def closeApp(query):
    speak("Closing the application Boss")
    if "one tab" in query:
        pyautogui.hotkey("ctrl", "w")
    elif "2 tabs" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        speak("all tabs closed")
    elif "3 tabs" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        speak("all tabs closed")
    elif "4 tabs" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        speak("all tabs closed")
    elif "5 tabs" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        speak("all tabs closed")
    elif "6 tabs" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        speak("all tabs closed")
    elif "7 tabs" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        speak("all tabs closed")
    else:
        keys= list(dictapp.keys())
        for app in keys:
            if app in query:
                # app = app.replace("close", "")
                # app = app.replace("friday", "")
                # app = app.replace("close with", "")
                # app = app.replace("close with google", "")
                # app = app.replace("close with", "")
                # app = app.replace(" ", "")
                os.system( f"taskkill /f /im {dictapp[app]}.exe")
                # speak(f"Closing {app} Boss")
            