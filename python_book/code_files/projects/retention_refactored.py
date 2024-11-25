"""
file: retention.py
author: Chris Cardenas (Refactored and changed by Mark Redd)
about:
This is a database for how many families enrolled in Ivy Hall throughout
the years, and the retention rate of each year

## pseudocode
1. First I want to open the json file to work with and if it doesn't exist, 
then I need to create one 
2. I want the terminal to ask me to ADD or RATES or QUIT. 
    - ADD will prompt me to put an enrollment year, then the student's first 
        and last name this would be organized as a dictionary with the key 
        being the year, and the value being a dictionary of the students' 
        names (key) and their grade (value). 
        
        If the year already exists, then it would append to the list in the 
        value for that year's key. 
        
        If the year doesn't exist, then it would create a new key with a 
        new list. 

    - RATES would check the whole list for me and tell me what the 
        retention rate is from year to year so it would say something like 
        "2020-2021 = 57% retention rate" so it would have to go through the 
        list of student names for the 2019-2020 school year and compare it to 
        the list of student names for the 2020-2021 school year and see what 
        percentage of names from the previous school year also appear on the 
        next school year's list it would have to exclude students who are in 
        the highest grade or left due to another reason, such as moving so 
        maybe that means I will need for the program to print how many names 
        were on the list from the previous year, and how many names stayed the 
        following year, so it can make my manual calculation easier instead of 
        me having to count each of the names and exclude the ones I know to 
        exclude
"""
# Chris: I have left some notes for you in comments. Try to address each one.

# you only need to import json for what you are doing here
# everything else is built in
import json


def get_year():
    # always validate input
    year = input("Enrollment year --> ")
    try:
        return int(year)
    except ValueError:
        print("Invalid Year.")
        return None
# put at least two lines of space between functions.
# this makes them easy to parse with your eye


def add(data):
    year = get_year()
    if not year: return

    # any input validation needed here?
    student = input("Student's full name --> ")
    data.setdefault(year, []).append(student)
    print("="*40)


def rates(data):
    year = get_year()
    if not year: return

    sorted_dict = sorted(data.items())
    alpha = dict(sorted_dict)

    sorted_keys = sorted(data.keys())
    # bug here for first year in list (Try getting rates for the first year.
    # Does it work how you want it to?)
    prev_year = sorted_keys[sorted_keys.index(year) - 1] 

    intersection = [
        thing for thing in data[year]
        if thing in data[prev_year]
    ]
    stayed = len(intersection)
    rate = stayed/len(alpha[prev_year])*100

    print("="*40)
    print("Retention rate for", year, "is:", rate, "%")
    print("="*40)


def read(data):
    print(f"{'key':<20}{'value':<20}\n"+'-'*40)
    for key, val in data.items():
        print(f"{key!s:<20}{', '.join(val):<20}")
    print('\n'+"="*40) 


def main():
    # escapes (i.e. \") are not needed for triple quotes
    prompt = """
    Type "add" to add student, "rates" to see 
    retention rates, "read" to read the list, or 
    "quit" to end program:
    --> """

    # just load the data once and save as needed.
    DATAFILE = "./retention_refactored.json"
    
    # for files, ask for forgiveness and not permisson
    # (seems counterintutive but uses less code)
    try: 
        open(DATAFILE).close()
    except FileNotFoundError:
        with open(DATAFILE, 'w') as f:
            json.dump({}, f)

    with open(DATAFILE, 'r') as f:
        data = json.load(f)
        # why is this line of code necessary?
        data = {int(key):val for key, val in data.items()}

    # group your code in logical ways to make it more readable
    running = True
    while running:
        choice = input(prompt)

        if "add" in choice:
            add(data)
            with open(DATAFILE, 'w') as f:
                json.dump(data, f, indent=4)
        elif "rates" in choice:
            rates(data)
        elif "read" in choice:
            read(data)
        elif "quit" in choice:
            running = False
        else:
            print("That is not an option.")
        # what if you want to delete a name or year?


if __name__ == '__main__': # figure out why this line is here
    main()