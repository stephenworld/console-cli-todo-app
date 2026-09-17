from utils.component import clear_terminal
import datetime
def add_task():
  clear_terminal()
  print("Create a new Task")

  task_name = input("Task Title: ").strip()
  while task_name == "":
    pass

  task_description = input("Task Description / Notes: ").strip()
  while task_description == "":
    pass

  has_due_date = input(f"Do you want to add a due date to Task {task_name}\nEnter [y/N]: ").strip()

  while has_due_date in ["y", "yes"]:
    now = datetime.date()

    year_input = input("Year: ").strip()
    month_input = input("Month: ").strip()
    day_input = input("Day: ").strip()

    """
    Validate year, month and day
    """

    recorded_date = {
      "year": now.year(),
      "month": now.month(),
      "day": now.day(),
    }
    due_date = {
      "year": year_input,
      "month": month_input,
      "day": day_input,
    }





  """
  Request Task Name
  Request 
  """

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