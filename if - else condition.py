#if - else conditions
print("----------------------------1----------------------------")
# 1 if- else condition by using camparition operators
# <, >, <=, >=, !=, ==
a = 3
b = 4
if a<b:
    print("a lesser")
else:
    print("a greater")

c = 3
d = 4
if c>d:
    print("c lesser")
else:
    print("c greater")

e = 3
f = 4
if e>=f:
    print("e lesser")
else:
    print("f greater")

g = 3
h = 4
if g<=h:
    print("g lesser")
else:
    print("h greater")

i = 3
j = 3
if i==j:
    print("Equal")
else:
    print("Not equal")

k = 3
l = 4
if k!=l:
    print("Equal")
else:
    print("Not equal")
print("----------------------------2----------------------------")
# 2 if- else condition by using logical operators
# and, or, not
a = 3
b = 4
if a<b and b==a:
    print("True")
else:
    print("False")

c = 3
d = 4
if a<b or b==a:
    print("True")
else:
    print("False")

e = 5
f = 7
if not e>f or f>e:
    print("True")
else:
    print("False")
print("----------------------------3----------------------------")
#3 if- else condition by using identify operators
#is, is not
a = 3
b = 4
if a is b:
    print("True")
else:
    print("False")

t = 3
h = 4
if t is not h:
    print("True")
else:
    print("False")
print("----------------------------4----------------------------")
#4 if- else condition by using membership operators
#in, not in
t = 3,4,5,6,7,8
if 4 in t:
    print("True")
else:
    print("False")

v = [3,4,5,6,7,8]
if 9 in v:
    print("True")
else:
    print("False")

l = (3,4,5,6,7,8)
if 9 not in l:
    print("True")
else:
    print("False")


















