Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #Arthematic operators
>>> a=5
>>> b=7
>>> print(a+b)
12
>>> print(a-b)
-2
>>> print(a*b)
35
>>> print(a//b)
0
>>> print(a/b)
0.7142857142857143
>>> print(a**b)
78125
>>> print(a%b)
5
>>> #Assignment operators --------------------------------------------------------------------------------
>>> t=3
>>> h=2
>>> t+=3
>>> t
6
>>> t-=h
t
4
t*=h
t
8
t//=h
t
4
t/=h
t
2.0
t**=h
t
4.0
h%=t
h
2.0
h*=t
h
8.0
h+=t
h
12.0
h-=t
h
8.0
h//=t
h
2.0
h/=t
h
0.5
#comparision operators--------------------------------------------------------------------------------------
v=7
l=5
v>l
True
v<l
False
v!=l
True
l!=v
True
v==l
False
v<=l
False
l>=v
False
l<=v
True
v>=l
True
#Logical operators----------------------------------------------------------------------------------------------------
t=8
h=12
t<h and h>t
True
t>h and h<t
False
t<=h and h>=t
True
t>=h or h>=t
True
t==h or t!=h
True
not True
False
not False
True
#Identify operators----------------------------------------------------------------------------------------------------------
c=7
type(c) is int
True
type(c) is not int
False
type(c) is float
False
d=7.5
type(d) is float
True
type(d) is not float
False
e="apple"
type(e) is str
True
type(e) is not str
False
f=5+7j
type(f) is complex
True
type(f) is not complex
False
g=True
type(g) is bool
True
type(g) is not bool
False
#Membership operators------------------------------------------------------------------------------------------
a=1,2,3,4,5
3 in a
True
6 in a
False
7 not in a
True
b="apple","banana","cherry","grapes"
"cherry" in b
True
"strawberry" not in b
True
"apple","banana" in b
('apple', True)
1,2 in a
(1, True)
2,6 in a
(2, False)
6,7 not in a
(6, True)
#Bitwise operators---------------------------------------------------------------------------------
a=2
b=3
a&b
2
a|b
3
bin(2)
'0b10'
bin(3)
'0b11'
a&b
2
v=8
-(v+1) # formula of ~
-9
~v
-9
h=-7
~h
6
-(h+1)
6
t=4
l=5
t^l
1
l^t
1

k=7
k<<2
28
m=8
m>>3
1
