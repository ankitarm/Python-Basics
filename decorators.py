# def function1():
#     print("hey hey")
# func = function1
# del function1
# func()

# def funret(num):
#     if num == 0:
#         return print
#     if num == 1:
#         return int
# a = funret(1)
# print(a)
#
# def executor(func):
#     func("this")
#
# executor(print)

# decorators
def dec1(func1):
    def nowexec():
        print("executing now")
        func1()
        print("executed")
    return nowexec

@dec1 #ankifun=dec1(ankifun)
def ankifun():
    print("ankifun")

ankifun()