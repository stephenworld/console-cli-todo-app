import json
from datetime import datetime


json_file = "data/data.json"

def clear_terminal():
  import sys
  sys.stdout.write("\033[H\033[2J\033[3J")
  sys.stdout.flush()

def is_valid_date(date_string):
  date_format="%Y-%m-%d"
  try:
    input_date = datetime.strptime(date_string, date_format).date()
    today = datetime.today().date()
    return input_date >= today

  except ValueError:
    return False

def is_valid_time(time_string):
  time_format = "%H-%M" 
  try:
    datetime.strptime(time_string, time_format)
    return True
  except ValueError:
    return False

def validate_time(time_string):
  hour, mins = time_string.split('-')
  return f"{int(hour):02d}", f"{int(mins):02d}"

def validate_date(date_string):
  year, month, day = date_string.split('-')
  return f"{int(year):04d}", f"{int(month):02d}", f"{int(day):02d}"


def update_data(task_data):
  try:
    with open(json_file, "r") as file:
      data = json.load(file)
  except FileNotFoundError:
    data = {}

  if data:
    next_id_int = max(int(key) for key in data.keys()) + 1
  else:
    next_id_int = 1

  new_id = f"{next_id_int:03d}"
  data[new_id] = task_data

  with open(json_file, "w") as file:
      json.dump(data, file, indent=2)

  print()
  print(f"Successfully added \"{task_data['name']}\" task with automatically generated ID: {new_id}")

def load_tasks():
  try:
    with open(json_file, "r") as file:
      data = json.load(file)
      data = update_task_status(data)
      
  except FileNotFoundError:
    data = {}

  return data

def update_task_status(data):
  for _, task in data.items():
    has_due_date = task["has_due"]
    
    status = task["status"]
    if status == "completed":
      continue

    if has_due_date:
      c_date = task["creation"]["date"]
      d_date = task["due_info"]["date"]
      c_time = task["creation"]["time"]
      d_time = task["due_info"]["time"]

      creation_str = f"{c_date['year']}-{c_date['month']}-{c_date['day']}"
      due_str = f"{d_date['year']}-{d_date['month']}-{d_date['day']}"

      creation_time_str = f"{c_time["hour"]}-{c_time["mins"]}"
      due_time_str = f"{d_time["hour"]}-{d_time["mins"]}"

      if (creation_str > due_str and creation_time_str > due_time_str):
        task["status"] = "overdue"
      else:
        task["status"] = "later"

  return data


def print_tasks(tasks):
  print("-"*125)
  print(f"| {"ID":<5} | {"Task Name":<40} | {"Creation Date":<25} | {"Due Date":<25} | {"Status":<15} |")
  print("-"*125)

  for task_id, task in tasks:
    task_name = task['name']
    task_creation = task['creation']['date']['year'] + "-" + task['creation']['date']['month'] + "-" + task['creation']['date']['day']
    has_due_date = task['has_due']
    dues_date = "N/A"

    if has_due_date:
      dues_date = task['due_info']['date']['year'] + "-" + task['due_info']['date']['month'] + "-" + task['due_info']['date']['day']

    status = task['status']
    print(f"| {task_id:<5} | {task_name:<40} | {task_creation:<25} | {dues_date:<25} | {status:<15} |")
    print("-"*125)


