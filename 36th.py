# Day 36
# lambda is powerfull if we use it as an anonymous function inside another function
def newFunction(v):
    return lambda a:a*v
double = newFunction(2)
triple = newFunction(3)
print(double(11))
print(triple(11))
