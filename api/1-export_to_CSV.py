#!/usr/bin/python3
"""task:1 extend your Python script to export data in the CSV format"""

import json
import requests
import sys
import csv


if __name__ == "__main__":
    url_users = 'https://jsonplaceholder.typicode.com/users/' + sys.argv[1]

    response = requests.get(url_users)
    if (response.ok):
        jData = json.loads(response.content)
        EMPLOYEE_NAME = jData["username"]
    else:
        response.raise_for_status()

    url_todos = "https://jsonplaceholder.typicode.com/todos"
    query = {'userId': sys.argv[1]}

    response = requests.get(url_todos, params=query)
    if (response.ok):
        jData = json.loads(response.content)

        csv_data = []
        for todo in jData:
            csv_data.append([sys.argv[1], EMPLOYEE_NAME, todo["completed"],
                            todo["title"]])

        filename = f"{sys.argv[1]}.csv"
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            for row in csv_data:
                writer.writerow(row)
    else:
        response.raise_for_status()
