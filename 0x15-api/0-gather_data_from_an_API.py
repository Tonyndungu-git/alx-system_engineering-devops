#!/usr/bin/python3

"""
Write a Python script that, using this REST API,
for a given employee ID, returns information about
his/her TODO list progress
"""
import requests
import sys


if __name__ == '__main__':

    id = sys.argv[1]
    task_title = []
    complete = 0
    total_task = 0
    url_user = "https://jsonplaceholder.typicode.com/users/" + id
    res = requests.get(url_user).json()
    name = res.get('name')
    url_task = "https://jsonplaceholder.typicode.com/todos/"
    res_task = requests.get(url_task).json()
    for task in res_task:
        if task.get('userId') == int(id):
            if task.get('completed') is True:
                task_title.append(task['title'])
                complete += 1
            total_task += 1
    print("Employee {} is done with tasks({}/{}):"
          .format(name, complete, total_task))
    for x in task_title:
        print("\t {}".format(x))
