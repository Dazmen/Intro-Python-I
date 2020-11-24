"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime

# get args from command line (also figure out how I am suppose to provide args in the command line from VScode???)
args = sys.argv

print(args) # to complete this as fully defined I would simply make input_y = args[1] and input_m = args[2]

def calender_func():
  # set up current date defaults
  today = datetime.today()
  year = today.year
  month = today.month

  # set up inputs for year and month
  input_y = input('What calendar year would you like to view? (digits only!) ex. 2019 ')
  input_m = input('What calendar mount would you like to view? (digits only! ex. 09) ')

  # conditionals to replace defaults with valid inputs
  if len(input_y) > 0 and len(input_y) <= 4 and input_y.isdigit():
    year = int(input_y)

  if len(input_m) > 0 and len(input_m) <= 2 and input_m.isdigit():
    month = int(input_m)

  print(calendar.month(year, month))

calender_func()

