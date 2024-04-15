#!/usr/bin/python3
"""task:0 gather data from an API"""

import requests
import sys


if __name__ == "__main__":
    """ahfjhwdf"""
    if len(sys.argv) < 2:
        print("wrong")
        sys.exit(1)

    user_id = sys.argv[1]
    url_users = 'https://jsonplaceholder.typicode.com/users/' + user_id

    try:
        response = requests.get(url_users)
        response.raise_for_status()
        user = response.json()
        EMPLOYEE_NAME = user["name"]
    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))
        sys.exit(1)

    url_todos = "https://jsonplaceholder.typicode.com/todos"
    query = {'userId': user_id}

    try:
        response = requests.get(url_todos, params=query)
        response.raise_for_status()
        todos = response.json()
        TOTAL_NUMBER_OF_TASKS = len(todos)

        NUMBER_OF_DONE_TASKS = 0
        for todo in todos:
            if todo["completed"] is True:
                NUMBER_OF_DONE_TASKS += 1

        print("Employee {} is done with tasks({}/{})".format(
            EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
        for todo in todos:
            if todo["completed"] is True:
                print("\t {}".format(todo["title"]))
    except requests.exceptions.RequestException as e:
        print("{}".format(e))
        sys.exit(1)
