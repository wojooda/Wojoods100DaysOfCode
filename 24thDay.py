#Day 24 :) python dictionaries
cardict = {"Brand": "Dodge", "Model": "Challenger", "Year": 2016}
print(cardict)
newdict = cardict.copy()
print(newdict)
mydict = dict(cardict)
print(mydict)
#nested dicts
familydict={
    "Child1": {"Name": "Wateen", "Year": 2006
    }, 
    "Child2": {"Name": "Saleh", "Year": 2009
    }, 
    "Child3": {"Name": "Mohammad", "Year": 2013
    }
}
print(familydict)
Child1= {"Name": "Wateen", "Year": 2006}
Child2= {"Name": "Saleh", "Year": 2009}
Child3= {"Name": "Mohammad", "Year": 2013}
onedict= {"Child1": Child1, "Child2": Child2, "Child3": Child3}
print(onedict)
diffrent_dict= dict(brand= "Chevrolet", Model= "Corvette", Year= "2018")
print(diffrent_dict)