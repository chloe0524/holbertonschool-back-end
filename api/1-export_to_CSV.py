#!/usr/bin/python3
"""task:1 extend your Python script to export data in the CSV format"""

import csv
import json
import requests
import sys


def hell_api(user_id):
    url_users = 'https://jsonplaceholder.typicode.com/users/' + user_id

    response = requests.get(url_users)
    if (response.ok):
        jData = json.loads(response.content)
        EMPLOYEE_NAME = jData["username"]
    else:
        response.raise_for_status()

    url_todos = "https://jsonplaceholder.typicode.com/todos"
    query = {'userId': user_id}

    response = requests.get(url_todos, params=query)
    if (response.ok):
        jData = json.loads(response.content)

        with open("{}.csv".format(user_id), "w", encoding='utf-8') as f:
            csv_writer = csv.writer(f, quoting=csv.QUOTE_ALL)
            for task in jData:
                csv_writer.writerow([user_id, EMPLOYEE_NAME,
                                    task.get("completed"),
                                    task.get("title")])
    else:
        response.raise_for_status()


if __name__ == "__main__":
    hell_api(sys.argv[1])
