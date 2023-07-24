#!/usr/bin/python3

import requests
import sys


def get_employee_todo(employ_id):
    """ gets details of what TODO has an employee done """
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/todos?userId={employee_id}"

    """fetch user datails"""
    user_response = requests.get(user_url)
    user_response.raise_for_status()
    user_data = user_response.json()
    employee_name = user_data["name"]

    """fetch user TODO"""
    todo_response = requests.get(todo_url)
    todo_response.raise_for_status()
    todo_data = todo_response.json()

    """calculate progress """
    total_tasks = len(todo_data)
    completed_tasks = sum(1 for task in todo_data if task["completed"])

    print(f"Employee {employee_name} is done with "
          f"tasks({completed_tasks}/{total_tasks}):")

    for task in todo_data:
        if task["completed"]:
            print(f"\t{task['title']}")


if __name__ == "__main__":

    employee_id = int(sys.argv[1])
    get_employee_todo(employee_id)
