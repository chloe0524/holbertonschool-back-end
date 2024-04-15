#!/usr/bin/python3
"""task:0 gather data from an API"""

import json
import requests
import sys


def hell_api():
    """ahfjhwdf"""
    url_users = 'https://jsonplaceholder.typicode.com/users/' + sys.argv[1]

    response = requests.get(url_users)
    jData = json.loads(response.content)
    EMPLOYEE_NAME = jData.get("name")

    url_todos = "https://jsonplaceholder.typicode.com/todos"
    query = {'userId': sys.argv[1]}

    response = requests.get(url_todos, params=query)
    jData = json.loads(response.content)
    TOTAL_NUMBER_OF_TASKS = len(jData)

    NUMBER_OF_DONE_TASKS = 0
    for todo in jData:
        if todo.get("completed") is True:
            NUMBER_OF_DONE_TASKS += 1

    print("Employee " + str(EMPLOYEE_NAME) + " is done with tasks(" +
          str(NUMBER_OF_DONE_TASKS) +
          "/" + str(TOTAL_NUMBER_OF_TASKS) + ")")
    for todo in jData:
        if todo.get("completed") is True:
            print("\t " + todo.get("title"))


if __name__ == "__main__":
    hell_api()
