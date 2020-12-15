# abstraction and encapsulation
# abstraction -
# encapsulation - implementation k details ko hide karna

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

    # class method
    @classmethod
    def changeleaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def altercon(cls,string):
        return cls(*string.split("-"))


harry = Employee("harry", 1234, "gdv hg")
rohan = Employee("rohan", 3241, "ffrfrf")
mohan = Employee.altercon("mohan-12345-vhysbch")

harry.changeleaves(56)
print(mohan.salary)
print(harry.no_of_leaves)
