import threading
import time
from systemMonitor import speak

def set_reminder(message,delay_in_minutes):
    def reminder_thread():
        time.sleep(delay_in_minutes * 60)
        speak(f"Reminder: {message}")
        
    thread=threading.Thread(target=reminder_thread)
    thread.start()
    speak(f"Reminder set for {delay_in_minutes} minutes from now: {message}")    
    