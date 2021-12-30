import json
import datetime

class DatabaseManager():
    def __init__(self, filename):
        self.filename = filename
        self.database = {
            'last saved' : 0,
            'db' : {}
        }
        self.load_database()
        

    def load_database(self):
        try:
            with open(self.filename, 'r') as f:
                self.database = json.load(f)
            self.save_database()
        except FileNotFoundError:
            self.save_database()
            
    
    def save_database(self):
        self.database['last saved'] = str(datetime.datetime.now())
        with open(self.filename, 'w') as f:
            json.dump(self.database, f, indent=4)

    
    def add_item(self, entry):
        self.database['db'][entry[0]] = {}
        self.database['db'][entry[0]]["phone"] = entry[1]
        self.database['db'][entry[0]]["email"] = entry[2]
        self.save_database()
    
    
    def remove_item(self, name):
        del self.database['db'][name]
        self.save_database()
        
    
    def get_database(self):
        return self.database['db']
        

    def __repr__(self):
        headers = ["Name", "Phone #", "Email"]
        out_string = '-'*72
        out_string += f"\n {headers[0]:<20} {headers[1]:<15} {headers[2]:<30}\n"
        out_string += '-'*72 + '\n'
        dbref = self.get_database()
        for key in dbref.keys():
            out_string += f" {key:<20} {dbref[key]['phone']:<15} {dbref[key]['email']:<30}\n"
        out_string += '-'*72
        return out_string


    
    def export(self, filename):
        with open(filename, 'w') as f:
            f.write(self.__repr__())




def test_dbman():
    dbman = DatabaseManager('data.json')
    print(dbman)
    dbman.add_item(["joe manyouare", 29382984, "coolguy@glasdkfj.com"])
    dbman.export("data.txt")
    print(dbman)
    dbman.remove_item("joe manyouare")
    print(dbman)
    


if __name__ == "__main__":
    test_dbman()