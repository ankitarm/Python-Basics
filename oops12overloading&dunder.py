class Employee:

    no_of_leaves = 8

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def printdetail(self):
        print(f"the name is {self.name}, salary is {self.salary} and role is {self.role}")

    @classmethod
    def changeleaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    # dunder method used for operator overloading

    def __add__(self, other):
        return self.salary+other.salary

    def __truediv__(self, other):
        return self.salary / other.salary

    def __repr__(self):
        return self.printdetail()



emp1 = Employee("emp1", 526, "drgvdrg")
# emp2 = Employee("emp2", 526, "fgbfgfg")
print(emp1)
# print(emp1+emp2)
# print(emp1/emp2)

