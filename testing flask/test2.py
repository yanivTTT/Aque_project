from commands import *
import requests
import json


response = get_tasks()
print "the response for the get_tasks() is: =={}==".format(response)

response = json.loads(response)
first_task_id = response[0].get('id')

response = change_completion(False, first_task_id)
print "the response for change_completion() is: =={}==".format(response)
print "now the list of tasks are: {}".format(get_tasks())
response = change_completion(True, first_task_id)
print "the response for change_completion() is: =={}==".format(response)
print "now the list of tasks are: {}".format(get_tasks())

response = get_task(first_task_id)
print "the response for get_task(task_id) is: =={}==".format(response)

response = add_task({"task": "i think i got this!!!", "completed": "true"})
print "the response for add_task(task) is: =={}==".format(response)
print ('the new tasks are: {}'.format(get_tasks()))

response = change_task(first_task_id, {"task": "changed===", "completed": "true"})
print "the response for add_task(task) is: =={}==".format(response)
print ('the new tasks are: {}'.format(get_tasks()))

response = delete_task(first_task_id)
print "the response for delete_task(task_id) is: =={}==".format(response)
print ('the new tasks are: {}'.format(get_tasks()))
