import datetime
import database
#Calander event, containing the name of the school
#the name of the event, and the date they have off
class Events:
   def __init__(self, group, dates, eventname):
      self.school = group
      self.date = dates
      self.name = eventname


class Assigned:
   def __init__(self, cover, covername, dates):
      self.covered = cover
      self.name = covername
      self.date = dates


#Prints out the welcome screen and gives options
def WelcomeScreen():
   choice = raw_input("Please enter a command:")
   if (choice == "show_curr_week"):
      #2015, 48 (Thanksgiving week)
      print_week(2015, 48)
      return None
   elif(choice == "show_next_week"):
      print_week(2015,49)
   elif (choice == "assign"):
      #Allows the PCP to assign a provider to their child on the
      #day given off, either themself of an ITP
      add_assign()
      return None
   elif choice =="quit":
       return True


#Assign care provider to day off
def add_assign():
   #Input
   covername = raw_input("Enter name of the care provider: ")
   coverdate = raw_input("Enter date of day they will cover: ")

   #Add to the database
   from database import add_assigned
   add_assigned(covername, coverdate)


#Add an event
def add_events():
   exit = 0
   while exit == 0:
      school = raw_input("Enter name of school: ")
      date = raw_input("Enter date (MM-DD-YY): ")
      name = raw_input("Enter holiday name: ")
      repeat = raw_input("Do you want to enter another? (y/n): ")
      if repeat.upper() == "N":
         exit = 1
      from database import add_event
      add_event(name, date, "1")

#Calculate the dates of the week given
def daysOfWeek(year, week):
   day = datetime.date(year, 2, 1)
   year, weekBase, dayBase = day.isocalendar()
   day += datetime.timedelta(1 - dayBase + (week - weekBase)*7)
   delta = datetime.timedelta(1)
   for i in range(0, 5):
      yield day
      day += delta
   #   yield day

def print_week(year, week):
   #Check if any days off


   #Print the dates of the week (M-F only)
   for d in daysOfWeek(year, week):
      print str(d)

#add_events();
from database import get_events
print get_events("1")
#print test[1]
#from database import add_school
#add_school("Westview")
#print_week(2015, 48)
