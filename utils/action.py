from utils.component import clear_terminal, is_valid_date, validate_date, is_valid_time, validate_time, update_data, load_tasks
from datetime import datetime

def add_task():
  clear_terminal()
  print("Create a new Task")

  task_name = input("Task Title: ").strip()
  while task_name == "":
    task_name = input("Task Title (REQUIRED): ").strip()

  task_description = input("Task Description / Notes: ").strip()
  while task_description == "":
    task_description = input("Task Description / Notes (REQUIRED): ").strip()

  has_due_date = input(f"Do you want to add a due date to Task {task_name}\nEnter [y/N]: ").strip().lower()
  due_date = "N/A"
  due_time = "N/A"

  while has_due_date in ["y", "yes"]:
    clear_terminal()

    due_date_input = input("Add your due date in this format [YYYY-MM-DD]: ").strip()
    is_date_valid = is_valid_date(due_date_input)

    while is_date_valid is False:
      clear_terminal()

      print(f"'{due_date_input}' Invalid. Try Current/Future Date.")
      due_date_input = input("Add your due date in this format [YYYY-MM-DD]: ").strip()
      is_date_valid = is_valid_date(due_date_input)

    clear_terminal()
    year, month, day = validate_date(due_date_input)

    due_date = {
      "year": year,
      "month": month,
      "day": day,
    }

    due_time_input = input("Add your remainder time in this format [Hour-Mins]: ")
    is_time_valid = is_valid_time(due_time_input)

    while is_time_valid is False:
      clear_terminal()
      print("Invalid Time. Try a valid [Hour(0-23)-Mins(0-59)] time")
      due_time_input = input("Add your remainder time in this format [Hour-Mins]: ")
      is_time_valid = is_valid_time(due_time_input)

    hour, mins = validate_time(due_time_input)
    clear_terminal()
    due_time = {
      "hour": hour,
      "mins": mins
    }

    break

  status = ""
  if has_due_date in ['yes', 'y']:
    status = "later"
  else:
    status = "undated"

  now = datetime.now()
  creation_date = {
    "year": str(now.year),
    "month": str(now.month),
    "day": str(now.day)
  }
  creation_time = {
    "hour": str(now.hour),
    "mins": str(now.minute)
  }

  task = {
    "name": task_name,
    "description": task_description,
    "creation": {
      "date": creation_date,
      "time": creation_time,
    },
    "has_due": has_due_date in ['yes', 'y'],
    "due_info": {
      "date": due_date,
      "time": due_time,
    },
    "status": "",
    "status": status
  }

  update_data(task)


def filter_task_by_status(status, tasks):
  filtered_task = [ (task_id, task) for task_id, task in tasks.items() if task["status"] == status]
  if not filtered_task:
    print(f"There isn't any tasks with the {status} status")
    return

  print("-"*110)
  print(f"| {"ID":<5} | {"Task Name":<25} | {"Creation Date":<25} | {"Due Date":<25} | {"Status":<15} |")
  print("-"*110)

  for task_id, task in filtered_task:
    task_name = task['name']
    task_creation = task['creation']['date']['year'] + "-" + task['creation']['date']['month'] + "-" + task['creation']['date']['day']
    has_due_date = task['has_due']
    dues_date = "N/A"
    if has_due_date:
      dues_date = task['due_info']['date']['year'] + "-" + task['due_info']['date']['month'] + "-" + task['due_info']['date']['day']
    status = task['status']

    print(f"| {task_id:<5} | {task_name:<25} | {task_creation:<25} | {dues_date:<25} | {status:<15}")


def view_tasks():
  clear_terminal()
  actions = ["view all task", "Filter by status"]

  for idx, action in enumerate(actions, 1):
    print(f"{idx}. {action}")

  tasks = load_tasks()
  user_action = input("Pick an action: ").strip()

  while user_action not in ["1", "2"]:
    clear_terminal()
    print("Valid actions are [1]View all tasks [2]Filter by status")
    user_action = input("Pick a valid action: ").strip()

  if user_action == "1":
    clear_terminal()
    if not tasks:
      print("Task is empty.")
      return

    print("-"*110)
    print(f"| {"ID":<5} | {"Task Name":<25} | {"Creation Date":<25} | {"Due Date":<25} | {"Status":<15} |")
    print("-"*110)

    for task_id, task in tasks.items():
      task_name = task['name']
      task_creation = task['creation']['date']['year'] + "-" + task['creation']['date']['month'] + "-" + task['creation']['date']['day']
      has_due_date = task['has_due']
      dues_date = "N/A"
      if has_due_date:
        dues_date = task['due_info']['date']['year'] + "-" + task['due_info']['date']['month'] + "-" + task['due_info']['date']['day']
      status = task['status']

      print(f"| {task_id:<5} | {task_name:<25} | {task_creation:<25} | {dues_date:<25} | {status:<15} |")

  elif user_action == "2":
    clear_terminal()
    statuses = ["later", "undated", "completed"]
    for idx, status in enumerate(statuses, 1):
      print(f"{idx} {status.capitalize()}")

    user_action = input("Select from the available statuses to filter: ").strip()
    clear_terminal()

    while user_action not in ["1", "2", "3"]:
      print("Valid actions are filter by [1]later [2]undated [3]completed")
      user_action = input("Select from the available statuses to filter: ").strip()

    if user_action == "1":
      filter_task_by_status("later", tasks)

    elif user_action == "2":
      filter_task_by_status("undated", tasks)

    elif user_action == "3":
      filter_task_by_status("completed", tasks)




def complete_task():
  clear_terminal()
  print("Complete Task")

def edit_task():
  clear_terminal()
  print("Edit task")

def exit():
  clear_terminal()
  return input("Are you sure you want to exit. (y/N): ").strip().lower()