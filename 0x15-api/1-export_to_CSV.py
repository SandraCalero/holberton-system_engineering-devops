#!/usr/bin/python3
"""Records all tasks that are owned by an employee
"""
import csv
import requests
from sys import argv

if __name__ == "__main__":
    employee_ID = int(argv[1])

    url = 'https://jsonplaceholder.typicode.com/'

    user = requests.get(url + 'users/' + str(employee_ID)).json()
    username = user['username']

    todo = requests.get(url + 'todos').json()
    todo_user = [task for task in todo if task['userId'] == int(employee_ID)]

    with open('{}.csv'.format(employee_ID), 'w', encoding='UTF8') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL)
        for task in todo_user:
            if task['userId'] == employee_ID:
                row.append(employee_ID)
                row.append(username)
                row.append(todo['completed'])
                row.append(todo['title'])
                writer.writerow(row)
                row = []
