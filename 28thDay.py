#while loop
i = 1
while i<5:
    print(i)
    i+=1

#while loop with break(توقف لمن توصل للشيء اللي قلتلها عليه)
w = 1
while w<7:
    print(w)
    if w==5:
        break
    w+=1

#while loop with continue (اذا وصل لأمر معين يسحب عليه ويكمل بعدو)
n = 0
while n<3:
    n+=1
    if n==1:
        continue
    print(n)

#while loop with else statement (تستمر لحد م يصير تتوقف حلقة وايل)
b = 1
while b<8:
    print(b)
    b+=1
else:
    print("b is no longer less than 8")

# هنا عشان نبين انو اذا كان الوايل غلط راح ينطبع الإيلس على طول
a = 10
while a<1:
    print(a)
    a+=1
else:
    print("a isn't less than 1") 
