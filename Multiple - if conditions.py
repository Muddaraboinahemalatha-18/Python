#Multiple - if conditions
print("---------------------------1------------------------")
#1 multiple - if conditions by using comparision operators
#<, >, <=, >=, ==, !=
a = 9
b = 11
if a>b:
    print("a is larger")
if b>a:
    print("b is larger")
if a==b:
    print("a is equal to b")
if a!=b:
    print("a is not equal to b")

c = 12
d = 30
if c<=d:
    print("c is smaller or esqual to d")
if d>=c:
    print("d is larger or equal to c")
if c==d:
    print("c is equal to d")
if c!=d:
    print("c is not equal to d")
print("---------------------------2------------------------")
#2 multiple - if conditions by using logical operators
# and, or, not
e = 12
f = 30
if e<=f and f>=e :
    print("e is smaller and larger to f")
if e==f or e!=f:
    print("e is equal to f or e is not equal to f")
if not e==23:
    print("True")
if not f==35:
    print("True")
print("---------------------------3------------------------")
#3 multiple - if conditions by using identify operators
# is, is not
g = 12
h = 30
if g is h :
    print("g is h")
if g is not h:
    print("g is not h")

k = 12
l = 12
if k is l :
    print("k is l")
if k is not l:
    print("k is not l")
print("---------------------------4------------------------")
#4 multiple - if conditions by using membership operators
#in, not in
v = [4,6,5,7,8,3,9,1]
if 5 in v :
    print("5 in v")
if 7 not in v:
    print("no")
if 12 not in v:
    print("12 not in v")


