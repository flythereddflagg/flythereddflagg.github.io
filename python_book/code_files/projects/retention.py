# retention.py

# This is a database for how many 
# families enrolled in Ivy Hall throughout
# the years, and the retention rate of each year

import json
import os.path
from os import path
from collections import defaultdict

# pseudocode
# first I want to open the json file to work with
# and if it doesn't exist, then I need to create one
# then I want the terminal to ask me to ADD or RATES or QUIT
# ADD will prompt me to put an enrollment year, then the student's first and last name
# this would be organized as a dictionary with the key being the year, and the value being a dictionary of the students' names (key) and their grade (value). If the year already exists, then it would append to the list in the value for that year's key. If the year doesn't exist, then it would create a new key with a new list.
# RATES would check the whole list for me and tell me what the retention rate is from year to year
# so it would say something like "2020-2021 = 57% retention rate"
# so it would have to go through the list of student names for the 2019-2020 school year and compare it to the list of student names for the 2020-2021 school year and see what percentage of names from the previous school year also appear on the next school year's list 
# it would have to exclude students who are in the highest grade or left due to another reason, such as moving
# so maybe that means I will need for the program to print how many names were on the list from the previous year, and how many names stayed the following year, so it can make my manual calculation easier instead of me having to count each of the names and exclude the ones I know to exclude

if os.path.isfile("retention.json"):
   with open("retention.json", 'r') as f:
     data = f.read()

# How do I make this make retention.json a dictionary?
else:
  with open("retention.json", 'w') as f:
    data = f.write("{}")

def add():
  year    = input("Enrollment year --> ")
  student  = input("Student's full name --> ")

  # Open the file "retention" and load it in as the variable "data"
  with open("retention.json") as f:
    data = json.load(f)

  # This line of code says, if the year inputted doesn't exist, create a new key and add family to that. If that year does exist, then just add family to that existing year.
  data.setdefault(year, []).append(student)
  
  # Now that you've added to "data" lets's dump that back in to the file "f" which is actually just the "retention" file
  with open("retention.json", "w") as f:
    json.dump(data, f)
  
  print("=========================================")


def rates():
  with open("retention.json") as f:
    data = json.load(f)
  
  sorted_dict = sorted(data.items())
  alpha = dict(sorted_dict)
  print(alpha)

  year = input("Retention for which year: ")
  # Go to the year previous and look at all of the family names
  sorted_keys = sorted(data.keys())
  prev_year = sorted_keys[sorted_keys.index(year) - 1]

  intersection = [
      thing for thing in data[year]
      if thing in data[prev_year]
  ]
  
  stayed = len(intersection)

  rate = (stayed/(len(alpha.get(prev_year))))*100
  
  print("=========================================")

  print("Retention rate for", year, "is:", rate, "%")

  print("=========================================")

def read():
  with open("retention.json") as f:
    data = json.load(f)

  print(data)

  print("=========================================")  

def main():
  prompt = """Type \"add\" to add student, \"rates\" to see retention rates, \"read\" to read the list, or \"quit\" to end program:
--> """
  
  running = True

  while running:
    choice = input(prompt)

    if "add" in choice:
      add()
    elif "rates" in choice:
      rates()
    elif "read" in choice:
        read()
    elif "quit" in choice:
      running = False
    else:
      print("That is not an option.")

main()