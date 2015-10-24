import os
import sys

scriptpath  = "database.py"
sys.path.append(os.path.abspath(scriptpath))
import database
def init_app(row, id):
    off = None
    while off is None:
        from calendar import WelcomeScreen
        off = WelcomeScreen()
    quit()


print("Welcome to Base Covered\n")

print("Commands:")
print("show_curr_week                                    ---Display current week")
print("show_next_week                                    ---Similar but display next week")
print("assign                                            ---Assign a person")
print("quit                                              ---Quit")


while True:
    u_id = raw_input("Enter Id: ")
    if u_id.isdigit():
        from database import get_pcp
        pcp_row = get_pcp(u_id)
        if pcp_row:
            print("Welcome "+pcp_row[0][1])
            init_app(pcp_row, u_id)
        else:
            print ("Error: User not found")
    else:
        break




