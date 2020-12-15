# ability to take various forms

class A:
    classvar1 = "im variable in class a"
    def __init__(self):
        self.var1 = "im in inside class a constructor"
        self.classvar1 = "instance var of class a"

class B(A):
    # class variable
    classvar2 = "im variable in class b"

    # instance variable
    def __init__(self):
        super().__init__()  # to call super/parent class constructor
        self.var1 = "im in inside class b constructor"
        self.classvar1 = "instance var of class b"
a = A()
b = B()

print(b.classvar1)
# this will always search for instance variable first in child class and
# then will search for instance variable in parent class
# if no instance var in any class then it will search for
# class var in child class and the in parent class


#