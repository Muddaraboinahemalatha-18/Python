#for loop()
print("------------------1------------------")
a = [10,20,30,40,50]
for i in a:
    print(i)
    
print("------------------2------------------")
a = [10,20,30,40,50]
for i in a:
    print(a)
    
print("-----------------3-------------------")
a = [10,20,30,40,50]
for i in a:
    print(i,end = ",")
    
print("-----------------4-------------------")
a = [10,20,30,40,50]
for i in a:
    print(i)
print(type(a))
print(type(i))

print("-------------------5-----------------")
a = ["apple","banana","cherry","grapes","mango"]
for i in a:
    print(i)
    print(type(a))
    print(type(i))
    
print("-----------------6-------------------")
b = (10,20,30,40,50)
for i in b:
    print(i)
print(type(b))
print(type(i))

print("-------------------7-----------------")
c = {10,20,30,40,50}
for i in c:
    print(i)
print(type(c))
print(type(i))

print("-----------------8-------------------")
a={"name":"hema","city":"vja","state":"ap","year":2026}
for i in a:
    print(i)
    
print("-----------------9-------------------")    
for i in a.keys():
    print(i)
    print(type(i))
    
print("------------------10------------------")   
for i in a.values():
    print(i)
    print(type(i))
    
print("------------------11------------------")  
for i in a.items():
    print(i)
    print(type(i))
    
print("------------------12------------------")    
b="codegnan"
for i in b:
    print(i)
    
print("-----------------13-------------------") 
c=[5.6,7.8]
for i in c:
    print(i)
    print(type(a))
    print(type(i))
    
print("------------------------------range()-------------------------")

#range()
#start,stop,step
print("-------------------1-----------------")
for i in range(11):
    print(i)
    
print("------------------2------------------") 
for i in range(5,12):
    print(i)
    
print("-----------------3-------------------")    
for i in range(1,10,1):
    print(i)
    
print("------------------4------------------") 
for i in range(0,19,2):
    print(i,end=" ")
    
print("------------------5------------------") 
for i in range(5,46,5):
    print(i,end=",")
    
print("-----------------6-------------------")   
for i in range(3,30,3):
    print(i,end=",")
