# class
class Employee:
    no_of_leaves = 10
    pass


# object
harry = Employee()
rohan = Employee()

# variables
harry.name = "harry"
harry.salary = 1234
harry.role = "hedwue"

rohan.name = "rohan"
rohan.salary = 4321
rohan.role = "srfdrgv"

# Property of class can be access through class and objects too
print(Employee.no_of_leaves)
print(harry.no_of_leaves)
print(rohan.no_of_leaves)

# Property of class cannot be modified by objects but can be by class itself
Employee.no_of_leaves = 9 #modifing
print(Employee.no_of_leaves)

harry.no_of_leaves = 8
print(Employee.no_of_leaves) #not changing

# harry.no_of_leaves = 8 is creating new instance variable for harry
# you cant overwrite the template and content in class using objects
# instance se class k variable ko nahi change kar sakte
print(harry.__dict__) # proof


