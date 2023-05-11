#Day 23 (Dictionaries 2)
bookdict={"Author": "Mosa almosa", "Book name": "Tathreeb", "Number of copies": "10000"}
if "Book name" in bookdict:
    print("Yes, 'Book name' is in this dict")
print(len(bookdict))
bookdict["Price"]= 29 # راح يضيف مفتاح وقيمة جديدة
print(bookdict)
bookdict.pop("Number of copies") # راح يحذف الشيء اللي حددناه له
print(bookdict)
bookdict.popitem() #راح يحذف آخر شيء
print(bookdict)
del bookdict["Author"]
print(bookdict)
bookdict.clear()
print(bookdict)