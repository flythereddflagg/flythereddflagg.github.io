<!-- Navigation -->

---

[Previous: 27 - Inheritance and Polymorphism](./27-Inheritance-and-Polymorphism.md) | [Table of Contents](./00-Table-of-Contents.md) | [Next: 29 - Comments and Code Documentation](./29-Comments-and-Code-Documentation.md)

---
<!-- End Navigation -->

# 28 - Modules

In this section we will explore how to connect python files together and make them work together. Also included in this section is an opportunity to get used to using classes and do more object oriented  programming.  Each file in Python is sometimes called a module. A module is simply a python file you can import and use its contents. You used some of the standard modules or libraries in [the section about imports](./23-Imports.md).

In this section we will begin learning how to build our own packages or libraries by connecting two modules together. In a later section, we will take what we accomplish here and make a complete (albeit simple) package that could be made into a distributable software. These will also be used in the next sections so **make sure you save these files for later**.

### The Email Database Manager

The following are two files that you will copy-paste into separate text files. (Please note that this is one of the rare times I will ask you to copy-paste code from this book.) The names of these files are indicated at the top. Put both files in a folder called "database_manager". The paths for these files are also indicated for clarity. These files serve as a sort of skeleton of a project you must complete using all you have learned so far. Take your time and get this project working as well as you possibly can. As always, the more you put into this the more you will get out of the experience. More specific information about the files is given below. Many of the same principles from your first project apply here. 

I have left multi-line comments under each label to guide your implimentation of this project. Do not delete these as these are the subject of the next section.

#### The Database Manager File

```python
# database_manager.py
# path <some root folder>/database_manager/database_manager.py
import json


class DatabaseManager():
    """
    Manages all aspects of the database including how and where data are stored.
    This database is contact list consisting of a collection of names with
    corresponding phone numbers and email addresses. This may be implimented as a
    dictionary (which sorts the list automatically) or a list. The exact structure 
    of the database is up to you but it might be a good idea to find out how others
    have done first.
    """
    def __init__(self, filename):
        """
        Loads the database based on the passed in filename. The database should
        come from a .json file and be stored in the class as a dictionary. This
        should call self.load_database() as its last step.
        """
        pass
        

    def load_database(self):
        """
        Loads the database from a .json file using Python's built in json 
        package. If the filename does not exist it should make an empty database
        and call self.save_database() to write the new database.
        """
        pass
        
    
    def save_database(self):
        """
        Saves the database to a .json file using Python's built-in json package.
        This should be called any time the database is altered.
        """
        pass
        
    
    def add_item(self, entry):
        """
        Adds and organizes an 'entry' consisting of an name, phone number and 
        email to the database it then saves the database.
        """
        pass
        
    
    def remove_item(self, name):
        """
        Removes an entry with ID 'name' from the database and then saves 
        the database.
        """
        pass
    

    def get_database(self):
        """
        Returns a reference or a copy of the database in some form to be 
        used elsewhere.
        """
        pass


    def __repr__(self):
        """
        Returns a string representation of the database. With this, the database
        may be printed or otherwise represented.
        """
        pass
   


def test_dbman():
    """
    A test function to ensure the database class performed as expected
    """
    pass


if __name__ == "__main__":
    test_dbman()
```

This file implements a class that will manage the database. The user interface class must have a reference to an instance of this class in the form of a class variable inside the `UserInterface` object (i.e. `self.dbman`) so that it can access all its methods. For this exercise you may use any format you wish. However, for this simple example I recommend using JavaScript Object Notation or JSON. I recommend this because Python has an excellent JSON library for storing data and JSON conveniently translates to common python objects such as dictionaries, lists, strings etc. You can learn how to use both the load and save features by looking at the corresponding Python documentation [here](https://docs.python.org/3/library/json.html#basic-usage) and reading about `json.load()` and `json.dump()`. The documentation strings under each label explain what should be implemented. Feel free to use your own creativity and what you have learned to implement this class. Finally, do not hesitate to add any methods or  make changes to names as you see fit. The `test_dbman()` function is there to allow you to test the class by itself before using it in the user interface. 

#### The User Interface File

```python
# user_interface.py
# path <some root folder>/database_manager/user_interface.py

from database_manager import DatabaseManager


class UserInterface():
    """
    Allows the user to access and use the features of the database without 
    having to know how to program.
    The user should be allowed to do a few basic things:
     - view the database
     - add an entry to the database
     - remove an entry from the database
     - export the database to a human-readable text file
     - exit the program
    
    Provided the user can do these thing easily and reliably, the program is
    successful.
    """
    
    def __init__(self, dbman):
        """
        sets up the UI and sets the self.dbman = dbman so the database may be
        accessed.
        """
        pass


    def mainloop(self):
        """
        Runs the mainloop of the program. This should include the following
        steps:
            1 - display information
            2 - prompt the user for input
            3 - process the input to get new information to display
            
        This also must exit the program when the user commands.
        """
        pass
         
         
    def display(self):
        """
        gets and displays information as given by the self.execute function.
        """
        pass
        
        
    def get_input(self):
        """
        Accepts user input by calling the built-in input() function
        """
        pass
    
    
    def execute(self):
        """
        Uses the information form user input to execute the program including
        accessing self.dbman to use database commands.
        """
        pass
        

    def export(self, filename):
        """
        Writes the database to a file with the path: 'filename'.
        May use a string representation of the database.
        """
        pass   
        
            
def run_ui_test():
    """
    This runs a UI test if we run it
    as the main Python program
    """
    db_manager = DatabaseManager('data.json')
    ui = UserInterface(db_manager)
    ui.mainloop()

if __name__ == '__main__':
    run_ui_test()

```

This file uses the `DatabaseManager` class to access the JSON files in a simple way. The user interface should contain a main-loop structure explained in the [Do a Project](./25-Do-a-Project.md) section. Try to make the user interface as intuitive and easy to use as possible. Again, the documentation strings under each label explain what should be implemented. Also as above, use your own creativity and what you have learned and add any methods or changes as you see fit. The `run_ui_test()` function is there to initiate the program. 

## Hone Your Skills

Once you have finished the main objective of this exercise you should have a working database program. Modify the program in the following ways:

- Add user interface features to always display the database on screen or only display it when it makes sense.
- Add error messages and make helpful info be printed out when the user gives bad input.

- Add home and work versions of emails and phone numbers so that multiple emails and phone numbers may be assigned to one person.
- Add options to the UI to allow different formats to be exported (e.g. .csv, .txt, or delimited by bars etc.). Implement at least two extra formats.
- Make a new type of database and implement it with your existing user interface. For example, this could be a car database using code from the previous sections.

## Advanced Mastery

- Look up the `curses` module in Python and use it to make a more advanced and easy-to-use user interface in the CLI.
- Look up `python tkinter` and begin learning how to build a non-CLI user interface. Use what you have learned to make a better UI for the database.

<!-- Navigation -->

---

[Previous: 27 - Inheritance and Polymorphism](./27-Inheritance-and-Polymorphism.md) | [Table of Contents](./00-Table-of-Contents.md) | [Next: 29 - Comments and Code Documentation](./29-Comments-and-Code-Documentation.md)

---
<!-- End Navigation -->
