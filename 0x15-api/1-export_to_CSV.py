#!/usr/bin/python3

import requests
import sys
import csv

def get_employee_todo(employee_id):
    """ gets details of what TODO has an employee done """
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/todos?userId={employee_id}"

    """fetch user datails"""
    user_response = requests.get(user_url)
    user_response.raise_for_status()
    user_data = user_response.json()
    employee_id = user_data["id"]
    employee_username = user_data["username"]

    """fetch user TODO"""
    todo_response = requests.get(todo_url)
    todo_response.raise_for_status()
    todo_data = todo_response.json()

    """ progress in csv format """
    filename = f"{employee_id}.csv"

    with open(filename, mode='w', newline='') as csvfile:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS",
                      "TASK_TITLE"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#        writer.writeheader()

        for task in todo_data:
                task_id = task["id"]
                task_title = task["title"]
                task_status = "COMPLETED" if task["completed"] else "NOT COMPLETED"
                writer.writerow({"USER_ID": employee_id,
                                 "USERNAME": employee_username,
                                 "TASK_COMPLETED_STATUS": task_status,
                                 "TASK_TITLE": task_title
                })




if __name__ == "__main__":

    employee_id = int(sys.argv[1])
    get_employee_todo(employee_id)
