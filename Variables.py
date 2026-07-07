Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Variables
print(1+2)
3
a=3
b=4
print(a+b)
7
c=5
print(c)
5
apple="fruite"
print(apple)
fruite
print("banana')
      
SyntaxError: unterminated string literal (detected at line 1)
print("banana")
      
banana
bat="ball"
      
print(bat)
      
ball
_=3
      
print(_)
      
3
_t=5
      
print(_t)
      
5
8=7
      
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
v8="peanut"
      
print(v8)
      
peanut
5h=2
      
SyntaxError: invalid decimal literal
t_7=12
      
print(t_7)
      
12
l=5
      
l
      
5
@=9
      
SyntaxError: invalid syntax
$=1
      
SyntaxError: invalid syntax
 z=3
      
SyntaxError: unexpected indent
apple banana="fruite"
      
SyntaxError: invalid syntax
apple_banana="fruite"
      
print(apple_banana)
      
fruite
a=6,b=7
      
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
a,b=8,7
      
print(a,b)
      
8 7
a=5:b=9
      
SyntaxError: invalid syntax
a=5:b=9
      
SyntaxError: invalid syntax
a=5;b=9
      
print(a,b)
      
5 9
a,b,c=1,2,3
      
print(a,b,c)
      
1 2 3
a,b,c,=1,2,3,4,5,6
      
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    a,b,c,=1,2,3,4,5,6
ValueError: too many values to unpack (expected 3, got 6)
a,b,c,d,e=1,2,3
      
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    a,b,c,d,e=1,2,3
ValueError: not enough values to unpack (expected 5, got 3)
a,b,c=(1,2,3)
...       
>>> print(a,b,c)
...       
1 2 3
>>> fname="Hemalatha"
...       
>>> lname="Muddaraboina"
...       
>>> print(fname+" "+lname)
...       
Hemalatha Muddaraboina
>>> print(fname,lname)
...       
Hemalatha Muddaraboina
>>> age=7
...       
>>> print(Age)
...       
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    print(Age)
NameError: name 'Age' is not defined. Did you mean: 'age'?
>>> print(age)
...       
7
