import json
from datetime import datetime

def log_command(command):
    entry ={"command": command, "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    try:
        with open("command_log.json", "a") as file:
            data = json.load(file)
            
    except:
        data = []
        
    data.append(entry)
    with open("command_log.json", "w") as file:
        json.dump(data, file, indent=4)    

def most_command():
    from collections import Counter
    try:
        with open("command_log.json", "r") as file:
            data = json.load(file)
            
        commands = [entry["command"] for entry in data]
      
        most_common = Counter(commands).most_common(1)
        return most_common[0][0] if most_common else "No commands logged yet."
    except:
       return "none."