#!/usr/bin/python3
""" Using what you did in the task #0, extend
    your Python script to export data in the JSON format"""

import json
import requests
import sys


if __name__ == "__main__":

    user = f"https://jsonplaceholder.typicode.com/users"
    todos = f"https://jsonplaceholder.typicode.com/todos"

    requests_user = requests.get(user)
    requests_todo = requests.get(todos)

    data_user = requests_user.json()
    data_todos = requests_todo.json()

    dict_data = {}

    for user in data_user:
        list_data = []

        for d in data_todos:
            if user["id"] == d["userId"]:
                task = {
                    "username": user["username"],
                    "task": d["title"],
                    "completed": d["completed"]
                    }
                list_data.append(task)

        dict_data[user["id"]] = list_data

    with open("todo_all_employees.json", "w") as fd:
        json.dump(dict_data, fd)
