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
  return hour, mins

def validate_date(date_string):
  year, month, day = date_string.split('-')
  return year, month, day


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
  except FileNotFoundError:
    data = {}

  return data

