# database_manager.py
import json


class DatabaseManager():
    """
    Manages all aspects of the database including how and where data are stored.
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