#!/usr/bin/python3
'''first api'''
import requests
import json
import sys


if __name__ == "__main__":
    '''api geter'''
    user_api = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(sys.argv[1]))
    todos_api = requests.get(
        'https://jsonplaceholder.typicode.com/todos/')
    user_data = user_api.text
    todos_data = todos_api.text
    user = json.loads(user_data)
    todos = json.loads(todos_data)
    completed = []
    all_todos = 0
    for todo in todos:
        if todo['userId'] == user['id']:
            if todo['completed']:
                completed.append(todo)
            all_todos += 1
    print(
        'Employee {} is done with tasks({}/{}):'
        .format(user['name'], len(completed), all_todos), file=sys.stdout)
    for finished_todo in completed:
        print('\t {}'.format(finished_todo['title']), file=sys.stdout)
