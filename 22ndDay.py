#python dictionaries
emptydict={}
print(emptydict)
infodict={"Name": "Wojood", "Grade": 100, "Speciality": "Cyber Security"}
print(infodict)
x = infodict["Name"]
print(x)
y = infodict.get("Grade")
print(y)
infodict["Grade"]= 1000
for x in infodict:
    print(x) #View keys
for x in infodict:
    print(infodict[x]) #View Values
for x in infodict.values(): #same as above, just a different way :)
    print(x)
print(infodict.values()) #Same as above'''
for x,y in infodict.items(): #displays all values and keys
    print(x,y)
print(infodict.items())
#Day 22 is done :)
