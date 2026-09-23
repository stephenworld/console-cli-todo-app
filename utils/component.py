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
  return int(hour), int(mins)

def validate_date(date_string):
  year, month, day = date_string.split('-')
  return int(year), int(month), int(day)


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
    due_data = task["due_info"]
    creation = task["creation"]

    if has_due_date:
      creation_full_date = f"{creation["date"]["year"]}-{creation["date"]["month"]}-{creation["date"]["day"]}"
      creation_time = f"{creation["time"]["hour"]}-{creation["time"]["mins"]}"

      due_full_date = f"{due_data["date"]["year"]}-{due_data["date"]["month"]}-{due_data["date"]["day"]}"
      due_time = f"{due_data["time"]["hour"]}-{due_data["time"]["mins"]}"

      if (creation_full_date > due_full_date or creation_time > due_time) and task["status"] != "completed":
        task["status"] = "overdue"

  return data


def print_tasks(tasks):
  print("-"*110)
  print(f"| {"ID":<5} | {"Task Name":<25} | {"Creation Date":<25} | {"Due Date":<25} | {"Status":<15} |")
  print("-"*110)

  for task_id, task in tasks:
    task_name = task['name']
    task_creation = task['creation']['date']['year'] + "-" + task['creation']['date']['month'] + "-" + task['creation']['date']['day']
    has_due_date = task['has_due']
    dues_date = "N/A"

    if has_due_date:
      dues_date = task['due_info']['date']['year'] + "-" + task['due_info']['date']['month'] + "-" + task['due_info']['date']['day']
    status = task['status']

    print(f"| {task_id:<5} | {task_name:<25} | {task_creation:<25} | {dues_date:<25} | {status:<15} |")
