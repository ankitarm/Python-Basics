# class
class Employee:
    no_of_leaves = 10

    # constructor
    def __init__(self, naam, paisa, kaam):
        self.name = naam
        self.salary = paisa
        self.role = kaam

    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"

# object
# harry = Employee()
# rohan = Employee()

# for passing args to the class we need to get a constructor
harry = Employee("harry", 1234, "gdv hg")

# variables
# harry.name = "harry"
# harry.salary = 1234
# harry.role = "hedwue"

# rohan.name = "rohan"
# rohan.salary = 4321
# rohan.role = "srfdrgv"
#
# print(rohan.printdetails())

print(harry.role)