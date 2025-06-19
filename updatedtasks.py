def mark_task_completed(task_name):
    try:
        with open("tasks.txt", "r") as file:
            lines= file.readlines()
           
            updated_lines = []
            found = False
            for line in lines:
               if task_name.lower() in line.lower() and "[ ]" in line:
                   updated_lines.append(line.replace("[ ]", "[x]"))
                   found = True
               else:
                   updated_lines.append(line)    
            with open("tasks.txt", "w") as file:
                file.writelines(updated_lines)
                
            return found
    except:
        return False        