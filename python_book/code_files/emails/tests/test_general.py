from emails.database_manager import DatabaseManager
from emails.user_interface import UserInterface


def test_dbman():
    dbman = DatabaseManager('data.json')
    dbman.add_item(["joe manyouare", 29382984, "coolguy@glasdkfj.com"])
    assert "joe manyouare" in dbman.__repr__()
    dbman.export("data.txt")
    dbman.remove_item("joe manyouare")
    assert not("joe manyouare" in dbman.__repr__())\
    

def test_ui():
    dbman = DatabaseManager('data.json')
    ui = UserInterface(dbman)
    