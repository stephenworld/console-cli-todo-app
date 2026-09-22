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
  filter_task_by_status = [ {task_id: task} for task_id, task in tasks.items() if task["status"] == status]
  return filter_task_by_status

def view_tasks():
  clear_terminal()
  actions = ["view all task", "Filter by status"]

  for idx, action in enumerate(actions, 1):
    print(f"{idx}. {action}")

  tasks = load_tasks()
  user_action = input("Pick an action: ").strip()

  while user_action not in ["1", "2"]:
    print("Valid actions are [1]View all tasks [2]Filter by status")
    user_action = input("Pick a valid action: ").strip()

  if user_action == "1":
    if not tasks:
      print("Task is empty.")
      return

    for idx, task in tasks.items():
      print(f"{idx}: {task}")

  elif user_action == "2":
    statuses = ["later", "undated", "completed"]
    for idx, status in enumerate(statuses, 1):
      print(f"{idx} {status.capitalize()}")

    user_action = input("Select from the available statuses to filter: ").strip()
    while user_action not in ["1", "2", "3"]:
      print("Valid actions are filter by [1]later [2]undated [3]completed")
      user_action = input("Select from the available statuses to filter: ").strip()

    if user_action == "1":
      status_data = filter_task_by_status("later", tasks)
      if not status_data:
        print("There isn't any tasks with the later status")
        return

      for task in status_data:
        print(task)

    elif user_action == "2":
      status_data = filter_task_by_status("undated", tasks)
      if not status_data:
        print("There isn't any tasks with the undated status")
        return

      for task in status_data:
        print(task)

    elif user_action == "3":
      status_data = filter_task_by_status("completed", tasks)
      if not status_data:
        print("There isn't any tasks with the completed status")
        return

      for task in status_data:
        print(task)



def complete_task():
  clear_terminal()
  print("Complete Task")

def edit_task():
  clear_terminal()
  print("Edit task")

def filter_tasks():
  clear_terminal()
  print("Filter tasks")

def exit():
  clear_terminal()
  return input("Are you sure you want to exit. (y/N): ").strip().lower()