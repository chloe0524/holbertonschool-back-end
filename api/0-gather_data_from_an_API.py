#!/usr/bin/python3
"""task:0 gather data from an API"""

import json
import requests
import sys


if __name__ == "__main__":
    """ahfjhwdf"""
    url_users = 'https://jsonplaceholder.typicode.com/users/' + sys.argv[1]

    response = requests.get(url_users)
    if (response.ok):
        jData = json.loads(response.content)
        EMPLOYEE_NAME = jData["name"]
    else:
        response.raise_for_status()

    url_todos = "https://jsonplaceholder.typicode.com/todos"
    query = {'userId': sys.argv[1]}

    response = requests.get(url_todos, params=query)
    if (response.ok):
        jData = json.loads(response.content)
        TOTAL_NUMBER_OF_TASKS = len(jData)

        NUMBER_OF_DONE_TASKS = 0
        for todo in jData:
            if todo["completed"] is True:
                NUMBER_OF_DONE_TASKS += 1

        print("Employee " + EMPLOYEE_NAME + " is done with tasks(" +
              str(NUMBER_OF_DONE_TASKS) +
              "/" + str(TOTAL_NUMBER_OF_TASKS) + ")")
        for todo in jData:
            if todo["completed"] is True:
                print("\t " + todo["title"])
    else:
        response.raise_for_status()
