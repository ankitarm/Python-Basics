# map(function,)

list1=["1","2","3","4","4"]
print(list1)
list1=list(map(int,list1))
print(map(int,list1))
print(list1)

num=[1,2,3,4,5,6,7]
n=list(map(lambda x:x*x,num))
print(n)

def square(a):
    return a*a
def cube(a):
    return a*a*a
li = [ square, cube ]
for e in range(5):
    v=list(map(lambda x:x(e),li))
    print(v)


# filter

a = list(filter(lambda x: x > 2, num))
print(a)

# joins

h = " @@".join(str(num))
print(h)

# reduce
from functools import reduce
prod = reduce(lambda x, y: x+y, num)
print(prod)