# user_interface.py
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
        Writes the database to a file pointed to by the variable 'filename'.
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
