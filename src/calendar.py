#Calander event, containing the name of the school
#the name of the event, and the date they have off
class Events:
   def __init__(self, group, dates, eventname):
      self.school = group
      self.date = dates
      self.name = eventname
   
EventsList = []

#Add an event
def add_event():
   exit = 0
   while exit == 0:
      school = raw_input("Enter name of school: ")
      date = raw_input("Enter date (MM/DD/YY): ")
      name = raw_input("Enter holiday name: ")
      x = Events([school], [date], [name])
      EventsList.append(x)
      repeat = raw_input("Do you want to enter another? (y/n): ")
      if repeat.upper() == "N":
         exit = 1

add_event()
for x in range(0, len(EventsList)):
   print EventsList[x].school
   print EventsList[x].date
   print EventsList[x].name

