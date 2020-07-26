from commands import *
import json


while True:
    command = raw_input("what you want to do? SEE TASKS/ADD TASK/REMOVE TASK/CHANGE TASK/CHANGE TASK STATUS  ")
    try:
        all_tasks = json.loads(get_tasks())[0]
    except:
        all_tasks = {}

    if command == 'SEE TASKS':
        print get_tasks()

    if command == 'ADD TASK':
        task = raw_input("what is the task?  ")
        new_task = {"task": task, "completed": "false"}
        new_task_id = add_task(new_task)
        new_task_id = json.loads(new_task_id)
        print("the new task id is: " + new_task_id['task_id'])

    if command == "REMOVE TASK":
        task_id = raw_input("what is the id of the task you want to delete? ")
        if task_id in all_tasks.values():
            delete_task(task_id)
            print("deleted")
        else:
            print('It dose not exist in here')
