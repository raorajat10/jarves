import re
from plyer import notification

def normalize(text):
    return re.sub(r'[^\w\s]', '', text.lower()).strip()

def mark_task_completed(task_text):
    try:
        norm_query = normalize(task_text)
        with open("tasks.txt", "r") as file:
            lines = file.readlines()

        updated = False
        new_lines = []

        for line in lines:
            if "." in line:
                idx, content = line.strip().split(".", 1)
            else:
                content = line.strip()
                idx = ""

            norm_content = normalize(content)

            if norm_query in norm_content and "✅" not in content:
                completed_line = f"{idx}.{content.strip()} ✅"
                new_lines.append(completed_line + "\n")
                updated = True

                # Show notification
                notification.notify(
                    title="✅ Task Completed",
                    message=f"Marked as done: {content.strip()}",
                    timeout=10
                )
            else:
                new_lines.append(line)

        # ✅ Now write ALL lines (updated and non-updated) back
        with open("tasks.txt", "w") as file:
            file.writelines(new_lines)

        return updated
    except Exception as e:
        print("Error in mark_task_completed():", e)
        return False
