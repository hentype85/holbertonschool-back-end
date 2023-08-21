#!/usr/bin/python3
""" Using what you did in the task #0, extend
    your Python script to export data in the CSV format
    """

import csv
import requests
import sys


if __name__ == "__main__":

    if len(sys.argv) == 2:
        id = sys.argv[1]

        user = f"https://jsonplaceholder.typicode.com/users/{id}"
        todos = f"https://jsonplaceholder.typicode.com/todos?userId={id}"

        requests_user = requests.get(user)
        requests_todo = requests.get(todos)

        data_user = requests_user.json()
        data_todos = requests_todo.json()

        username = data_user.get("username")

        file_name = f"{id}.csv"

        # open the CSV file in write mode and create a csv.writer object
        with open(file_name, "w") as fd:
            txt = csv.writer(fd, quoting=csv.QUOTE_ALL)
            # write each row to the CSV file
            for t in data_todos:
                txt.writerow([id, username, t["completed"], t["title"]])
