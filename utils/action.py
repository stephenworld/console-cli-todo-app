from utils.component import clear_terminal, is_valid_date, validate_date, is_valid_time, validate_time, update_data
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


  task = {
    "name": task_name,
    "description": task_description,
    "has_due": has_due_date in ['yes', 'y'],
    "due_info": {
      "date": due_date,
      "time": due_time,
    },
    "status": "",
    "record_time": {}
  }

  update_data(task)

def view_tasks():
  clear_terminal()
  print("View all tasks")

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