# if - condition
print("--------------------------------1---------------------------------")
# 1 if condition by using comparision operators
# <, >, <=, >=, !=, ==
print("--------1-------")
a = 10
b = 20
if a<b:
    print("True")
print("--------2-------")   
a = 6
b = 9
if a>b:
    print("True")
print("--------3-------")
a = 6
b = 9
if a>b:
    print("False")
print("--------4-------")
c = 5
d = 7
if c <= d:
    print("True")
print("--------5-------")
e = 30
f = 18
if e>=f:
    print("True")
print("--------6-------")
g = 7
h = 7
if g==h:
    print("Equal")
print("--------7-------")
i = 5
j = 6
if i != j:
    print("Not Equal")
print("--------8-------")
v = int(input("enter no:"))
if v <= 4:
        print("True")
print("--------9-------")
t = int(input("Enter no :"))
if t == 5:
        print("True")
print("--------10-------")
s1 = "apple"
s2 = "banana"
if s1 == s2:
    print("equal")
print("--------11-------")
s1 = "apple"
s2 = "apple"
if s1 == s2:
    print("Equal")
print("--------12-------")
s1 = input("Enter s1 :")
s2 = input("Enter s2 :")
if s1 == s2:
        print("True")
print("--------------------------------2--------------------------------")
# 2 if condition by using logical operators
# and, or, not
print("--------1-------")
a = 4
b = 5
if a<b and b>a:
    print("True")
print("--------2-------")
c = 9
d = 11
if c<=d and d>=c:
    print("True")
print("--------3-------")
e = 8
f = 12
if e!=f or f==e:
    print("True")
print("--------4-------")
g = 5
h = 9
if not g<h:
    print("less")
print("--------5-------")
i = 5
j = 9
if i>j:
    print("less")
print("--------6-------")
k = 5
l = 9
if not k<l and l>k:
    print("less")
print("--------7-------")
k = 5
l = 9
if  k<l and l>k:
    print("less")
print("---------------------------------3-------------------------------")
# 3 if condition by using identifying operators
# is, is not
print("--------1-------")
a = 7
if type(a) is int:
    print("True")
print("--------2-------")
b = 8
if type(a) is not int:
    print("False")
print("--------3-------")
c = int(input("enter no: "))
if type(a) is int:
    print("True")
print("--------4-------")
d = float(input("enter no: "))
if type(d) is float:
    print("True")
print("--------5-------")
e = str(input("enter string: "))
if type(e) is str:
    print("True")
print("--------6-------")
f = str(input("enter string: "))
if type(f) is not str:
    print("True")
print("---------------------------------4-------------------------------")
# 4 if condition by using membership operators
# in, not in
print("--------1-------")
a = 1,3,4,5,6,7
if 3 in a:
    print("True")
print("--------2-------")
b = 3,4,5,6,7,8,9
if 10 not in b:
    print("True")
print("--------3-------")
c = 22,55,44,33,77
if 66 in c:
    print("True")
print("--------4-------")
e = [5,6,7,8,3,4,2]
f = int(input("enter no : "))
if f in e:
    print("True")
print("--------5-------")
d = int(input("enter no: "))
if 30 in d:
    print("True")#error'''



    




