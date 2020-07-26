import requests

BASE_URL = "http://127.0.0.1:5000/"


def get_tasks():
    response = requests.request("GET", BASE_URL + 'tasks')
    return response.text.encode('utf8')


def get_task(task_id):
    response = requests.request("GET", BASE_URL + 'tasks/' + str(task_id))
    return response.text.encode('utf8')


def change_completion(completed, task_id):
    if completed:
        response = requests.post(BASE_URL + "tasks/" + str(task_id) + "/completed")
        return response
    elif not completed:
        response = requests.post(BASE_URL + "tasks/" + str(task_id) + "/incomplete")
        return response


def add_task(task_to_add):

    payload = "{\"task\": \"" + task_to_add["task"] + "\",\"completed\": \"" + task_to_add['completed']+"\"}"
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", BASE_URL + "tasks", headers=headers, data=payload)
    return response.text.encode('utf8')


def delete_task(task_id):
    response = requests.delete(BASE_URL + "tasks/" + str(task_id))
    return response.text.encode('utf8')


def change_task(task_id, new_task):
    payload = "{\"task\": \"" + new_task["task"] + "\",\"completed\": \"" + new_task['completed'] + "\"}"
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("put", BASE_URL + "tasks/" + str(task_id), headers=headers, data=payload)
    return response.text.encode('utf8')
