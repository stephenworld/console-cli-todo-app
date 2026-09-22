from utils.action import exit
actions = ["Add task", "View tasks", "Complete task", "Edit task", "Exit"]

def welcome():
  print("To-Do CLI Application\n")

  for idx, action in enumerate(actions):
    print(f"{idx+1}. {action}")

  user_action = input(f"\nEnter a valid action [1 - {len(actions)}]: ").strip()
  valid_actions = [str(nbr) for nbr in range(1, len(actions)+1, 1)]

  while user_action not in valid_actions:
    user_action = input(f"'{user_action}' is an invalid action. Try [1 - {len(actions)}]").strip()

  return user_action

def handle_restart():
  print()
  res = input("Do you want to do anything else. (y/N): ").strip().lower()
  while res not in ["yes", "y"]:
    return 
    
  return res
