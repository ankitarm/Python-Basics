# object oriented programming-just a method of programin, objects are derived from class method
#object-instance of class
#DRY-do not repeat yourself

class Student:
    pass


harry = Student()
larry = Student()

# variables
harry.name = "harry"
harry.std = 12
harry.sec = 1

print(harry.name, harry.std, harry.sec)

print(harry, larry) # two objects at different memory location

