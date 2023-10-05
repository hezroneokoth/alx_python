#!/usr/bin/python3
"""Gather Data from API.

This script uses REST API (with employee data)
and returns info about the employee's TODO list progress."""

import requests
import sys

def get_employee_data(employee_id):

    # defines the base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # gete employee's details
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    user_data = user_response.json()

    # get the employee's TODO list
    todos_response = requests.get(f"{base_url}/users/{employee_id}/todos")
    todos_data = todos_response.json()

    return user_data, todos_data

# checks if the correct no of args is provided
# and if the argument is a valid integer
def main():
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    user_data, todos_data = get_employee_data(employee_id)

    # processes the data
    total_tasks = len(todos_data)
    completed_tasks = sum(1 for todo in todos_data if todo["completed"])

    # displays the information
    print(f"Employee {user_data['name']} is done with tasks({completed_tasks}/{total_tasks}):")
    for todo in todos_data:
        if todo["completed"]:
            print(f"\t{todo['title']}")

if __name__ == "__main__":
    main()