#!/usr/bin/python3
""" Write a Python script that, using this REST API,
    for a given employee ID, returns information
    """

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

        name = data_user.get("name")

        tasks = []
        for t in data_todos:
            if t.get("completed"):
                tasks.append(t.get("title"))

        print("Employee {} is done with tasks({}/{}):".format(
            name, len(tasks), len(data_todos)))
        for i in tasks:
            print("\t {}".format(i))
