decimal = [0.1, 0.2, 0.3, 0.4, 0.5]
print(decimal)
print(decimal[3])
for x in decimal:
    print(x)
decimal[2]= 0.0
print(decimal)
del decimal[0]
print(decimal)
del decimal
print(decimal) #an eroor message will appear :)
newlist = ["A","L","W","S","M","B"]
print(newlist)
del newlist[0]
print(newlist)
del newlist[2]
print(newlist)
#hopefully it works