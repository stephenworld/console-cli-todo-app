from utils.welcome import welcome, handle_restart
from utils.action import add_task, view_tasks, complete_task, edit_task, exit
from utils.component import clear_terminal

clear_terminal()
user_action = welcome()

while True:
  if user_action == "1":
    add_task()

    res = handle_restart()
    if res in ["yes", "y"]:
      clear_terminal()
      print("Welcome Back!!!")
      user_action = welcome()
    else:
      clear_terminal()
      print("Successfully Exited the program")
      break

  elif user_action == "2":
    view_tasks()
    res = handle_restart()
    if res in ["yes", "y"]:
      clear_terminal()
      print("Welcome Back!!!")
      user_action = welcome()
    else:
      clear_terminal()
      print("Successfully Exited the program")
      break

  elif user_action == "3":
    complete_task()

    res = handle_restart()
    if res in ["yes", "y"]:
      clear_terminal()
      print("Welcome Back!!!")
      user_action = welcome()
    else:
      clear_terminal()
      print("Successfully Exited the program")
      break

  elif user_action == "4":
    edit_task()

    res = handle_restart()
    if res in ["yes", "y"]:
      clear_terminal()
      print("Welcome Back!!!")
      user_action = welcome()
    else:
      clear_terminal()
      print("Successfully Exited the program")
      break

  elif user_action == "5":
    res = exit()
    if res == "yes" or res == "y":
      clear_terminal()
      print("Successfully Exited the program")
      break

    else:
      clear_terminal()
      print("Program Restart")
      user_action = welcome()

  else:
    print("Invalid Action. Try [1 - 6]")
