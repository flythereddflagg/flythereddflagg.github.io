from emails.database_manager import DatabaseManager
import os

if os.name == 'nt':
    CLEAR = 'cls'
else:
    CLEAR = 'clear'

class UserInterface():
    
    menu = """
             - Main Menu - 
Please select one of the following options:
1 - View database
2 - Edit database
3 - Export database
0 - Quit"""
    
    def __init__(self, dbman):
        self.current_view = self.menu
        self.dbman = dbman


    def mainloop(self):
        self.running = True
        
        os.system(CLEAR)
        while self.running:
            self.display()
            self.get_input()
            os.system(CLEAR)
            self.execute()
            os.system(CLEAR)
        os.system(CLEAR)

            
    def display(self):
        print("""
        ---   Email Database Manager   ---""")
        print(self.current_view)
    
    
    def get_input(self):
        self.current_input = input("\n --> ")
    
    
    def execute(self):
        if self.current_input.startswith('0'):
            self.running = False
        elif self.current_input.startswith('1'):
            self.current_view = str(self.dbman) + self.menu
        elif self.current_input.startswith('2'):
            self.edit_database()
            self.current_view = str(self.dbman) + self.menu
        elif self.current_input.startswith('3'):
            filename = input("Specify the filename: ")
            self.dbman.export(filename)
            self.current_view = f"Database exported to {filename}\n" + self.menu
        else:
            self.current_view = "\n"+"-"*5+" invalid input!\n" + self.menu
    
    
    def edit_database(self):
        selection = 1
        msg = ""
        while selection != 'q':
            os.system(CLEAR)
            self.current_view = str(self.dbman) + msg
            self.display()
            selection = input("""
               --- Edit Mode ---
               
add <name> - add <name> to database 
rm <name>  - remove <name> from database
q          - exit edit mode
--> """)
            data = selection.split()
            if data[0] == 'add' and len(data) > 1:
                name = ' '.join(data[1:])
                phone = input("Phone number: ")
                email = input("Email: ")
                self.dbman.add_item([name,phone,email])
                msg = f"""
data added to database: 
name          : {name}
phone number  : {phone}
email address : {email}"""
            elif data[0] == 'rm' and len(data) > 1:
                try:
                    self.dbman.remove_item(' '.join(data[1:]))
                    msg = f"\n{data[1]} removed from database"
                except KeyError as err:
                    msg = f"\n{err} not found in database"
                    
            elif data[0] == 'q':
                pass
            else:
                msg = "\n\t--- invalid input! ---\n"

        
        
            
def run_ui_test():
    """
    This runs a UI test if we run it
    as the main Python program
    """
    filename = input("give a database filename: ")
    db_manager = DatabaseManager('data.json')
    ui = UserInterface(db_manager)
    ui.mainloop()

if __name__ == '__main__':
    run_ui_test()
