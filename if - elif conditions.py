#if - elif conditions
print("--------------------1----------------------------")
#1 if - elif conditions by using comparition operators
#<, >, <=, >=, ==, !=
a = 2
b = 4
if a< b:
    print("less")
elif b>a :
    print("greater")

c = 5
d = 9
if c<= d:
    print("c less or equal")
elif c>=d:
    print("c greater or equal")
elif d>c:
    print("d greater")

e = 5
f = 9
if e== f:
    print("e equal f")
elif e!=f:
    print("e not equal f")
elif f>e:
    print("f greater")
print("------------------------2------------------------")
#2 if - elif conditions by using logical operators
#and, or, not
l = 2
k = 4
if l ==2 and k==5:
    print("True")
elif l==2 or k==7 :
    print("greater")

n = 2
m = 4
if not n< m:
    print("less")
elif not m<n :
    print("greater")
print("-----------------------3-------------------------")
#3 if - elif conditions by using identify operators
#is, is not
c = 2
d = 2
if c is d:
    print("True")
elif d is not c:
    print("False")

e = 2
f = 5
if e is f:
    print("True")
elif e is not f:
    print("False")
print("------------------------4------------------------")
#4 if - elif conditions by using membership operators
#in, not in
t = 22,33,44,55,66
if 77 in t:
    print("True")
elif 77 not in t:
    print("Yes")

v = (22,33,44,55,66)
if 55 in v:
    print("True")
elif 55 not in v:
    print("Yes")

h = [3,5,4,6,7,1,8]
if 1 in h:
    print("True")
elif 9 not in h:
    print("Yes")


