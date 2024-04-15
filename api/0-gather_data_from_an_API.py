#!/usr/bin/python3
"""task:0 gather data from an API"""

import json
import requests
import sys


def hell_api():
    """ahfjhwdf"""
    url_users = 'https://jsonplaceholder.typicode.com/users/' + sys.argv[1]

    response = requests.get(url_users)
    if (response.ok):
        jData = json.loads(response.content)
        name = jData["name"]
    else:
        response.raise_for_status()

    url_todos = "https://jsonplaceholder.typicode.com/todos"
    query = {'userId': sys.argv[1]}

    response = requests.get(url_todos, params=query)
    if (response.ok):
        jData = json.loads(response.content)
        nb_tasks = len(jData)

        completed = 0
        for todo in jData:
            if todo["completed"] is True:
                completed += 1

        print("Employee " + name + " is done with tasks(" + str(completed) +
              "/" + str(nb_tasks) + ")")
        for todo in jData:
            if todo["completed"] is True:
                print("\t " + todo["title"])
    else:
        response.raise_for_status()


if __name__ == "__main__":
    hell_api()
