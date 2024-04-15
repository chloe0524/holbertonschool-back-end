#!/usr/bin/python3
"""task:3 extend your Python script to export data in the JSON format ++++"""

import json
import requests
import sys


def hell_api():
    url_users = 'https://jsonplaceholder.typicode.com/users'

    response = requests.get(url_users)
    if (response.ok):
        users = json.loads(response.content)
    else:
        response.raise_for_status()

    all_tasks = {}

    for user in users:
        user_id = str(user["id"])
        EMPLOYEE_NAME = user["username"]

        url_todos = "https://jsonplaceholder.typicode.com/todos"
        query = {'userId': user_id}

        response = requests.get(url_todos, params=query)
        if (response.ok):
            jData = json.loads(response.content)

            tasks = []
            for task in jData:
                tasks.append({
                    "username": EMPLOYEE_NAME, "task": task.get("title"),
                    "completed": task.get("completed")
                })

            all_tasks[user_id] = tasks
        else:
            response.raise_for_status()

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_tasks, json_file)


if __name__ == "__main__":
    hell_api()
