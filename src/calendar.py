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
      #print_week(2015, 48)
      print_week(2015, 44)
      return True
   elif(choice == "show_next_week"):
      print_week(2015,49)
   elif (choice == "assign"):
      #Allows the PCP to assign a provider to their child on the
      #day given off, either themself of an ITP
      add_assign()
      return True
   elif choice == "school":
       return True
   elif choice =="quit":
       return False




#Assign care provider to day off
def add_assign():
   #Input
   covername = raw_input("Enter name of the care provider: ")
   coverdate = raw_input("Enter date of day they will cover(MM-DD-YYYY): ")

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

#Prints out all of the days for the week
def print_week(year, week):
   #Store all of the Days & Holidays
   WeekList = []
   HolidayDates = []
   HolidayNames = []
   AssignedDates = []
   AssignedNames = []


   #Print the dates of the week (M-F only)
   for d in daysOfWeek(year, week):
      WeekList.append(d)
      from database import get_events
      school_events = get_events("1")
      for x in range(0, len(school_events)):
         #There is a day off this week
         if str(school_events[x][1]) == str(d):
            HolidayDates.append(d)
            HolidayNames.append(school_events[x][2])
      from database import get_all_assigned
      assigned_dates = get_all_assigned()
      for i in range(0, len(assigned_dates)):
         if (str(assigned_dates[i][2]) == str(d)):
            AssignedDates.append(d)
            AssignedNames.append(assigned_dates[i][1])

   #Replace Holiday into original class list
   for x in range(0, len(HolidayDates)):
      #Find spot
      for i in range(0, len(WeekList)):
         #Replace
         if (str(WeekList[i]) == str(HolidayDates[x])):
            WeekList[i] = str(HolidayDates[x]) + " School Closed -   " + str(HolidayNames[x]) + "  covered by - ***NOBODY***  "
            #Check assigned
            for j in range (0, len(AssignedDates)):
               if (str(HolidayDates[x])) == (str(AssignedDates[j])):
                 WeekList[i] = WeekList[i].strip(" covered by - ***NOBODY***")
                 WeekList[i] = WeekList[i] + " covered by - "
                 WeekList[i] = WeekList[i] + AssignedNames[j]

   #Print the entire week out (M-F only)
   for x in range(0, len(WeekList)):
      print WeekList[x]


print_week(2015, 44)

#Prints out all of the days off for that specific school
def print_school():
   from database import get_events
   school_events = get_events("1")
   for x in range(0, len(school_events)):
       print str(school_events[x][1]) + " " + school_events[x][2]

#from database import add_assigned
#add_assigned("Rob", "10-30-15")
