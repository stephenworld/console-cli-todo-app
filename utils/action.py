from utils.component import clear_terminal

def add_task():
  clear_terminal()
  print("Create a new Task")

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