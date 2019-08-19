from emails.database_manager import DatabaseManager
from emails.user_interface import UserInterface

import os


def test_dbman():
    filename = 'data.json'
    name = "joe manyouare"
    export = 'data.txt'
    data = [name, 29382984, "coolguy@glasdkfj.com"]
    
    dbman = DatabaseManager(filename)
    try:
        with open(filename, 'r') as f:
            contents = f.read()
        file_exists = True
    except FileNotFoundError:
        file_exists = False
    
    assert file_exists
    
    dbman.add_item(data)
    assert name in dbman.__repr__()
    
    
    dbman.export(export)
    try:
        with open(export, 'r') as f:
            contents = f.read()
        export_exists = True
    except FileNotFoundError:
        export_exists = False
        
    assert export_exists
    
    dbman.remove_item(name)
    assert not(name in dbman.__repr__())
    os.remove(filename)
    os.remove(export)

    

def test_ui():
    filename = 'data.json'
    name = "joe manyouare"
    export = 'data.txt'
    data = [name, 29382984, "coolguy@glasdkfj.com"]
    
    dbman = DatabaseManager(filename)
    ui = UserInterface(dbman)
    os.remove(filename)