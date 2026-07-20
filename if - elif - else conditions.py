#if - elif - else conditions
print("------------------------------1--------------------------")
#1 if - elif - else conditions by using comparition operators
#<, >, <=, >=, ==, !=
a = 2
b = 4
if a< b:
    print(" a less")
elif b>a :
    print("b greater")
else:
    print("equal")

a = 5
b = 9
if a<= b:
    print("a less or equal")
elif b>=a:
    print("b greater or equal")
elif a == b:
    print("a equal b")
else:
    print("not equal")
print("------------------------------2--------------------------")
#2 if - elif - else conditions by using logical operators
# and, or, not
a = 2
b = 2
if a< b and b>a:
    print("Yes")
elif a==b or a!=b  :
    print("No")
else:
    print("False")

c = int(input("Enter the c value: "))
d = int(input("Enter the d value: "))
if c< 3 and d>10:
    print("True1")
elif c==5 or d!=7  :
    print("True2")
else:
    print("False")

e = 5
if e == 6:
    print("True1")
elif not e == 7  :
    print("True2")
else:
    print("False")
print("------------------------------3--------------------------")
#3 if - elif - else conditions by using identify operators
# is, is not
g = 2
h = 2
if g is h:
    print("True1")
elif g is not h  :
    print("True2")
else:
    print("False")

i = 2
j = 3
if i is j:
    print("True1")
elif i is not j  :
    print("Yes")
else:
    print("False")
print("------------------------------4--------------------------")
#4 if - elif - else conditions by using membership operators
#in, not in
v = [3,5,6,4,8,6,74]
if 85 in v:
    print("Yes")
elif 77 not in v:
    print("No")
else:
    print("False")
