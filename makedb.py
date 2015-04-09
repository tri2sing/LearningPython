from person import Person, Manager

bob = Person('Bob Smith')
sue = Person('Sue Jones', job='dev', pay=100000)
tom = Manager('Tom Jones', 50000)

import shelve
db = shelve.open('persondb')                 # Filename where objects are stored
for obj in (bob, sue, tom):                  # Use object's name attr as key
    db[obj.name] = object                    # Store object on shelve by key
db.close()                                   # Close after making changes

