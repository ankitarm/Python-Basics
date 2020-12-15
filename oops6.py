# abstraction and encapsulation
# abstraction -
# encapsulation - implementation k details ko hide karna
# static topic
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

    # method just to print
    # sometimes u need to run just the employee object on this and not for other objects
    @staticmethod
    def printgood(string):
        print("this is good "+string)

# all attributes and methods are inherited from employee
class Programmer(Employee):

    no_of_leaves = 56

    def __init__(self, naam, paisa, kaam, li):
        self.name = naam
        self.salary = paisa
        self.role = kaam
        self.list1 = li

    def printprog(self):
        return f"Programmers Name is {self.name}. Salary is {self.salary} and role is {self.role} and knows language {self.list1}"


harry = Employee("harry", 1234, "gdv hg")
rohan = Employee("rohan", 3241, "ffrfrf")


mohan = Programmer("mohan", 1234, "gdvhhfgbhg", ["python"])
karan = Programmer("karan", 3241, "ffrfjhvbrf", ["python","cpp"])

print(karan.printprog())
print(karan.no_of_leaves)
