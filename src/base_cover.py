import os
import sys

scriptpath  = "database.py"

sys.path.append(os.path.abspath(scriptpath))

import database

print("Welcome to Base Cover\n")

print("Commands:")
print("show_wk <month> <start day of the week(Sunday)>  ---Displays the current week")
print("show_next <month> <start day of the week(Sunday)> ---Similar but display next week")
print("assign <Person> <date>                            ---Assign a person")
print("school <school name>                              ---Show school's events")
print("quit                                              ---Quit")


