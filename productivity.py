from systemMonitor import speak

def calculate_productivity():
    # Count focus sessions
    try:
        with open("focus.txt", "r") as file:
            focus_sessions = len(file.readlines())
            speak(f"You have completed {focus_sessions} focus sessions today.")
    except:
        focus_sessions = 0

    # Count completed tasks only
    try:
        with open("tasks.txt", "r") as file:
            lines = file.readlines()
            completed_tasks = [line for line in lines if "[x]" in line]
            pending_tasks = [line for line in lines if "[ ]" in line]
            completed = len(completed_tasks)
            pending = len(pending_tasks)
            speak(f"You have completed {completed} tasks. {pending} are still pending.")
    except:
        completed = 0

    # Productivity score: weighted
    score = min(100, focus_sessions * 20 + completed * 15)
    speak(f"Your productivity score for today is {score} out of 100.")
