#!/usr/bin/python3
"""Script that, using a REST API, for a given employee ID, returns
information about his/her TODO list progress
"""

from json import load
import requests
from sys import argv

if __name__ == "__main__":
    employee_ID = argv[1]

    url = 'https://jsonplaceholder.typicode.com/'

    user = requests.get(url + 'users/' + employee_ID).json()
    employee_name = user['name']

    todo = requests.get(url + 'todos').json()
    todo_user = [task for task in todo if task['userId'] == int(employee_ID)]
    todo_completed = [task for task in todo_user if task['completed'] is True]
    number_of_done_tasks = len(todo_completed)
    total_number_of_tasks = len(todo_user)

    print('Employee {} is done with tasks({}/{}):'.format(employee_name,
          number_of_done_tasks, total_number_of_tasks))
    for task in todo_completed:
        task_title = task['title']
        print('\t {}'.format(task_title))
