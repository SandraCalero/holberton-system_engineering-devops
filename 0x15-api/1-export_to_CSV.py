#!/usr/bin/python3
"""Records all tasks that are owned by an employee
"""
import csv
import json
import requests
import sys


if __name__ == '__main__':
    employee_ID = int(sys.argv[1])
    todos_data = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = json.loads(todos_data.text)
    employee_data = requests.get('https://jsonplaceholder.typicode.com/users')
    employees = json.loads(employee_data.text)
    '''Creating row'''
    row = []
    '''Getting employee username'''
    for empl in employees:
        if empl['id'] == employee_ID:
            employee_username = empl['username']
    '''Write to csv file'''
    with open('{}.csv'.format(employee_ID), 'w', encoding='UTF8') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL)
        for todo in todos:
            if todo['userId'] == employee_ID:
                row.append(employee_ID)
                row.append(employee_username)
                row.append(todo['completed'])
                row.append(todo['title'])
                writer.writerow(row)
                row = []
