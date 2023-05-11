def my_fun(food):
    for x in food:
        print(x)
fruits = ['apple', 'banana', 'cherry']
my_fun(fruits)

#Arbitrary arguments 'used when u don't know how many arguments will be passed to the function' add * before parameter
def arbitraryFun(*kids): #this will make it accpet infinite num of parameters
    print("The youngest child is " + kids[2])
arbitraryFun("Asalah", "Lujain", "Wateen", "Saleh", "Mohammad")
