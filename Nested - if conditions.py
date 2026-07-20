#nested - if conditions
print("----------------------------1--------------------------")
#1 nested - if conditions by using comparision operators
#<, >, <=, >=, ==, !=
a = 2
b = 4
if a<b :
    print("a less")
    if b >a:
        print("b greater")

c = 2
d = 2
if c==d :
    print("equal")
    if d >c:
        print("d greater")

e = 2
f = 4
if e<f :
    print("e less")
    if f >e:
        print("f greater")
    else:
        print("equal")

a = 2
b = 4
if a==b :
    print("Equal")
    if b!=a:
        print("Not equal")
else:
    print("True")

a = 2
b = 4
if a<b :
    print("a less than b")
    if b >a:
        print("b greater than a")
    elif a!=b:
        print("not equal")
print("----------------------------2--------------------------")
#2 nested - if conditions by using logical operators
#and, or, not
a = 2
b = 4
if a<b and b>a :
    print("a less than b")
    if b >a or b==a :
        print("b greater than a or equal")
elif not a!=b:
        print("not equal")
print("----------------------------3--------------------------")
#3 nested - if conditions by using identify operators
# is, is not
h = 2
t = 5
if h is not t :
    print("h is not t")
    if h is t:
        print("h is t")
print("----------------------------4--------------------------")
#4 nested - if conditions by using identify operators
# in, not in
v  = 2,5,7,8,3,30,25
if 7 in v :
    print("7 in v")
    if 35 not in v:
        print("35 not in v")


    

