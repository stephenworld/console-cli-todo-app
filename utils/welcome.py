actions = ["Add task", "View tasks", "Complete task", "Edit task", "Filter tasks", "Exit"]

def welcome():
  """
  Interphase
  """
  print("To-Do CLI Application\n")

  for idx, action in enumerate(actions):
    print(f"{idx+1}. {action}")

  user_action = input(f"\nEnter a valid action [1 - {len(actions)}]: ").strip()
  valid_actions = [str(nbr) for nbr in range(1, len(actions)+1, 1)]

  while user_action not in valid_actions:
    user_action = input(f"'{user_action}' is an invalid action. Try [1 - {len(actions)}]").strip()

  return user_action

def add_task():
  """
  Add Task
  """
  