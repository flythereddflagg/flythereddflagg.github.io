from emails.database_manager import DatabaseManager

def test_dbman():
    dbman = DatabaseManager('data.json')
    dbman.add_item(["joe manyouare", 29382984, "coolguy@glasdkfj.com"])
    assert "joe manyouare1" in dbman.__repr__()
    dbman.export("data.txt")
    dbman.remove_item("joe manyouare")
    