# :shipit: API

## :round_pushpin: Task 0: Gather Data from an API

**Description:**
This task involves writing a Python script to fetch information about an employee's TODO list progress from a given REST API.

**Requirements:**
- Use of `urllib` or `requests` module.
- The script must accept an integer as a parameter, representing the employee ID.
- Display employee TODO list progress in a specific format.

**Usage:**
```
python3 0-gather_data_from_an_API.py <employee_id>
```

## :round_pushpin: Task 1: Export to CSV

**Description:**
Extending the previous script to export data to CSV format.

**Requirements:**
- Record all tasks owned by the employee.
- Format: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
- File name: `<USER_ID>.csv`

**Usage:**
```
python3 1-export_to_CSV.py <employee_id>
```

## :round_pushpin: Task 2: Export to JSON

**Description:**
Extending the original script to export data to JSON format.

**Requirements:**
- Record all tasks owned by the employee.
- Format: `{ "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}`
- File name: `<USER_ID>.json`

**Usage:**
```
python3 2-export_to_JSON.py <employee_id>
```

## :round_pushpin: Task 3: Dictionary of List of Dictionaries

**Description:**
Extending the original script to export data for all employees in JSON format.

**Requirements:**
- Record all tasks from all employees.
- Format: `{ "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}`
- File name: `todo_all_employees.json`

**Usage:**
```
python3 3-dictionary_of_list_of_dictionaries.py
```
