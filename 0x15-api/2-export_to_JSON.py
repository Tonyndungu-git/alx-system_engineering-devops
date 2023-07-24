#!/usr/bin/python3
"""
Write a Python script that's  using a REST API,
and then exports data into a json format.
"""
import json
import requests
import sys


if __name__ == '__main__':
    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                         .format(id)).json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                         .format(sys.argv[1])).json()

    with open("{}.json".format(id), "w") as user_id:
        json.dump({id: [{
                'task': task.get('title'),
                'completed': task.get('completed'),
                'username': users.get('username')
            } for task in todos]}, user_id)
