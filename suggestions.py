from brianTTS import speak
from datetime import datetime
from commandLogger import log_command, most_command
from reminder import set_reminder
from core_utils import takeCommand

def suggestions():
    current_time = datetime.now().strftime("%H:%M")
    hour = int(current_time.split(":")[0])

    if 6 <= hour < 12:
        speak("How about starting your day with some exercise or a healthy breakfast?")
    elif 12 <= hour < 14:
        speak("Maybe take a short break and grab some lunch?")
    elif 14 <= hour < 18:
        speak("Would you like me to enter focus mode or set a reminder for something?")
        response = takeCommand().lower()

        if "focus" in response or "yes" in response:
            speak("Activating Focus Mode now.")
            import os
            os.system("python FocusMode.py")

        elif "reminder" in response:
            speak("What would you like to be reminded about?")
            msg = takeCommand()

            speak("In how many minutes?")
            try:
                delay = int(takeCommand().split()[0])
                set_reminder(msg, delay)
            except:
                speak("Sorry Boss, I couldn't set that reminder.")

        else:
            speak("Alright. Let me know when you're ready.")
    
    elif 18 <= hour < 19:
        speak("Ready for the gym? It's a great way to unwind after a long day.")

    elif 19 <= hour < 22:
        speak("Want to review your tasks for the day or plan for tomorrow?")
    
    else:
        speak("Good night! It's time to relax and get ready for bed.")

    favorite_command = most_command()
    if favorite_command != "none":
        speak(f"By the way, your most used command is '{favorite_command}'.")
