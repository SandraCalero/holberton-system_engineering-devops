#!/usr/bin/python3
"""Records all tasks that are owned by an employee
"""
import csv
import requests
from sys import argv

if __name__ == "__main__":
    employee_ID = argv[1]

    url = 'https://jsonplaceholder.typicode.com/'

    user = requests.get(url + 'users/' + employee_ID).json()
    username = user['username']

    todo = requests.get(url + 'todos').json()
    todo_user = [task for task in todo if task['userId'] == int(employee_ID)]

    with open(employee_ID + '.csv', 'w') as filename:
        writer = csv.writer(filename, quoting=csv.QUOTE_ALL)
        for task in todo_user:
            data = [employee_ID, username, task['completed'], task['title']]
            writer.writerow(data)
