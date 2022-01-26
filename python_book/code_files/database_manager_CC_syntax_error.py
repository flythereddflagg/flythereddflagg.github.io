# database_manager.py
# path <some root folder>/database_manager/database_manager.py
import json
import os.path
from os import path


class DatabaseManager():
    """
    Manages all aspects of the database including how and where data 
    are stored. This database is contact list consisting of a 
    collection of names with corresponding phone numbers and email 
    addresses. This may be implimented as a dictionary (which sorts 
    the list automatically) or a list. The exact structure of the  
    out how others database is up to you but it might be a good idea
    to find have done first.
    """
    def __init__(self, filename):
        """
        Loads the database based on the passed in filename. The 
        database should come from a .json file and be stored in 
        the class as a dictionary. This should call 
        self.load_database() as its last step.
        """
        self.filename = filename
        # What's this for in the __init__ function? Does it 
        # pass the file into each of the following functions?
        
        # Mark: This line guarentees that the database loads upon
        # object instantiation.
        self.load_database() 



    def load_database(self):
        """
        Loads the database from a .json file using Python's built  
        in json package. If the filename does not exist it should 
        make an empty database and call self.save_database() to write
        the new database.
        """
        # Use the json package here!!!!
        
        if os.path.isfile(self.filename):
            with open(self.filename, "r") as f:
                data = f.read()

        else:
            with open(self.filename, "w") as f:
                data = f.write("{}")

        return data
        # self.save_database(data)


    def save_database(self):
        """
        Saves the database to a .json file using Python's built-in 
        json package. This should be called any time the database 
        is altered.
        """
        # with open({self.filename}, "r") as f:
        #     data = json.load(f)

        with open(self.filename, "w") as f:
            json.dump(data, f)


    def add_item(self, name, number, email):
        """
        Adds and organizes an 'entry' consisting of an name,
        phone number and email to the database it then saves
        the database.
        """
        self.entry = entry
        self.number = number
        self.email = email

        data = self.load_database

        data.setdefault(name, []).extend((number, email) # <-- syntax error is here

        self.save_database() # <-- but python does not realize it until it gets here (Why?)


