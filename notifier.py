from datetime import datetime, timedelta
from plyer import notification
import json

while True:
    try:
        with open('tasks.json', 'x+') as f:
            tasks = []
    except FileExistsError:
        with open('tasks.json') as f:
            try:
                tasks = json.load(f)
            except json.decoder.JSONDecodeError:
                tasks = []

    for task in tasks:
        task_name = task[0]

        try:
            task_time = datetime(*list(map(int, task[1].split())))

    
            if datetime.now() >= task_time:
                notification.notify(
                    title='TODO',
                    message= task_name
                )
            
                task[1] = (task_time + timedelta(days=1)).strftime("%Y %m %d %H %M")
                with open('tasks.json', 'w') as f:
                    json.dump(tasks, f)
        
        except TypeError:
            pass
