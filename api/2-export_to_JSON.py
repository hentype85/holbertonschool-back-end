#!/usr/bin/python3
""" Using what you did in the task #0, extend
    your Python script to export data in the JSON format."""

import requests
import json
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

        dict_data = {}
        list_data = []

        for d in data_todos:
            task = {
                "task": d["title"],
                "completed": d["completed"],
                "username": username
            }
            list_data.append(task)

        dict_data[id] = list_data

        with open(f"{id}.json", "w") as fd:
            json.dump(dict_data, fd)
