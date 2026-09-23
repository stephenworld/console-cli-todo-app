from utils.component import clear_terminal, is_valid_date, validate_date, is_valid_time, validate_time, update_data, load_tasks, print_tasks
from datetime import datetime

json_file = "data/data.json"

def add_task():
  clear_terminal()
  print("Creating a new Task\n")

  task_name = input("Task Title: ").strip()
  while task_name == "":
    task_name = input("Task Title (REQUIRED): ").strip()

  task_description = input("Task Description / Notes: ").strip()
  while task_description == "":
    task_description = input("Task Description / Notes (REQUIRED): ").strip()

  print()
  has_due_date = input(f"Do you want to add a due date to Task '{task_name}'\nEnter [y/N]: ").strip().lower()
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
      "year": str(year),
      "month": str(month),
      "day": str(day),
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
      "hour": str(hour),
      "mins": str(mins)
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

  clear_terminal()
  update_data(task)


def filter_task_by_status(status, tasks):
  filtered_task = [ (task_id, task) for task_id, task in tasks.items() if task["status"] == status]
  if not filtered_task:
    print(f"There isn't any tasks with the {status} status")
    return

  print_tasks(filtered_task)

def view_tasks():
  clear_terminal()
  actions = ["view all task", "Filter by status"]
  print("View / Filter Task\n")
  for idx, action in enumerate(actions, 1):
    print(f"[{idx}] {action}")

  tasks = load_tasks()
  print()
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

    print("Showing All Available tasks\n")
    print_tasks(tasks.items())

  elif user_action == "2":
    clear_terminal()
    statuses = ["later", "undated", "completed"]
    print("Filter by Status\n")
    for idx, status in enumerate(statuses, 1):
      print(f"[{idx}] {status.capitalize()}")

    print()
    user_action = input("Select from the available statuses to filter: ").strip()
    clear_terminal()

    while user_action not in ["1", "2", "3"]:
      print("Valid actions are filter by [1]later [2]undated [3]completed")
      user_action = input("Select from the available statuses to filter: ").strip()

    if user_action == "1":
      print("Filtering tasks scheduled for LATER\n")
      filter_task_by_status("later", tasks)

    elif user_action == "2":
      print("Filtering by UNDATED tasks\n")
      filter_task_by_status("undated", tasks)

    elif user_action == "3":
      print("Filtering by COMPLETED tasks\n")
      filter_task_by_status("completed", tasks)


def complete_task():
  clear_terminal()
  tasks = load_tasks()

  if not tasks:
    print("Task is empty.")
    return

  print("Update task status\n")
  print_tasks(tasks.items())
  print()
  user_action = input("Select a task ID that has been completed: ").strip()
  while user_action == "":
    print("Task can't be empty")
    user_action = input("Select a task ID that has been completed: ").strip()

  available_task_id = [id for id in tasks]
  while user_action not in available_task_id:
    print(f"Invalid task ID try any of these ID's {available_task_id}")
    user_action = input("Select a task ID that has been completed: ").strip()

  print()
  certain_action = input(f"Are you sure you want to mark '{tasks[user_action]["name"]}' as completed [y/N]: ").strip()
  clear_terminal()
  if certain_action in ["yes", "y"]:
    tasks[user_action]["status"] = "completed"
    import json
    with open(json_file, "w") as file:
      json.dump(tasks, file, indent=2)
    print(f"Task '{user_action}' with the name '{tasks[user_action]["name"]}' has been completed")
  else:
    print("Action cancled")

def edit_task():
  clear_terminal()
  tasks = load_tasks()
  if not tasks:
    print("Task is empty.")
    return

  print_tasks(tasks.items())
  print()
  user_action = input("Select a task ID you want to edit: ").strip()
  while user_action == "":
    print("Task can't be empty")
    user_action = input("Select a task ID you want to edit: ").strip()

  available_task_id = [id for id in tasks]
  while user_action not in available_task_id:
    print(f"Invalid task ID try any of these ID's {available_task_id}")
    user_action = input("Select a task ID you want to edit: ").strip()

  task_data = tasks[user_action]

  clear_terminal()
  print(f"Showing full details for task {user_action}\n")
  
  name = task_data["name"]
  description = task_data["description"]
  creation = task_data["creation"]
  has_due = task_data["has_due"]
  due = task_data["due_info"]

  creation_full_date = f"{creation["date"]["year"]}-{creation["date"]["month"]}-{creation["date"]["day"]}"
  creation_time = f"{creation["time"]["hour"]}-{creation["time"]["mins"]}"

  print(f"Task Name: {name}")
  print(f"Task Description: {description}")
  print(f"Creation Date / Time: {creation_full_date} / {creation_time}")

  available_edit_options = [ "Name", "Description", "Creation" ]

  if has_due:
    due_full_date = f"{due["date"]["year"]}-{due["date"]["month"]}-{due["date"]["day"]}"
    due_time = f"{due["time"]["hour"]}-{due["time"]["mins"]}"
    print(f"Due Date / Time: {due_full_date} / {due_time}")
    available_edit_options = [ "Name", "Description", "Creation", "Due Date" ]

  print()
  print("Things editable")

  for idx, option in enumerate(available_edit_options, 1):
    print(f"[{idx}] {option}")

  print()
  action = input("What would you edit: ").strip()
  actions = [str(idx) for idx,_ in enumerate(available_edit_options, 1)]

  while action not in actions:
    print(f"Valid actions are {actions}")
    action = input("What would you edit: ").strip()

  if action == "1":
    """
    Edit task Name
    """
    print("Edit task Name")
  elif action == "2":
    """
    Edit task Description
    """
    print("Edit task Description")
  elif action == "3":
    """
    Edit task creation date
    """
    print("Edit task creation date")
  elif action == "4":
    """
    Edit task Due Date
    """
    print("Edit task Due Date")
  else:
    print("Invalid Actions")

  


def exit():
  clear_terminal()
  return input("Are you sure you want to exit. (y/N): ").strip().lower()