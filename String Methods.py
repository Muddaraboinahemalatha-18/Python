Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #String Methods
>>> #len()
>>> a="codegnan"
>>> len(a)
8
>>> b="python course"
>>> len(b)
13
>>> c=""
>>> len(c)
0
>>> d=" "
>>> len(d)
1
>>> #count() method
>>> e="twinkle twinkle little star"
>>> count(e)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    count(e)
NameError: name 'count' is not defined. Did you mean: 'round'?
>>> e.count("twinkle")
2
>>> e.count("k")
2
e.count(" ")
3
e.count("t")
5
e.count("")
28
e.count("h")
0
#Find the string
v="vijayawada"
v.find("w")
6
v.find("a")
3
v.find("v")
0
v.find("h")
-1
v.find("l")
-1
v.find()
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    v.find()
TypeError: find expected at least 1 argument, got 0
#Escape sequences
#\n--> new line or next line
#\t--> tab space(4 to 8)
h="name\n emailid\t mobileno\n college\t branch"
h
'name\n emailid\t mobileno\n college\t branch'
print(h)
name
 emailid	 mobileno
 college	 branch
l="Name: Hemalatha\n Emailid: hema@gmail.com\t Mobileno: 6452846924\n College: VITW\t Branch: CSE-DS"
print(l)
Name: Hemalatha
 Emailid: hema@gmail.com	 Mobileno: 6452846924
 College: VITW	 Branch: CSE-DS
k="Name: Hemalatha\nEmailid: hema@gmail.com\tMobileno: 6452846924\nCollege: VITW\tBranch: CSE-DS"
print(k)
Name: Hemalatha
Emailid: hema@gmail.com	Mobileno: 6452846924
College: VITW	Branch: CSE-DS
#replace() method
x="I am in vijayawada"
x.replace("in","from")
'I am from vijayawada'
y="You have to study for your success"
y.replace("have to","should")
'You should study for your success'
z="course"
z.replace("c","k")
'kourse'
r="work work until succeed"
r.replace("work","wait")
'wait wait until succeed'
r.replace("wait","work",1)
'work work until succeed'
g="wait work until succeed"
g.replace("wait","hard")
'hard work until succeed'
t="work work until succeed"
t.replace("work","wait",1)
'wait work until succeed'
#upper() method
a="code"
a.upper()
'CODE'
a[0].upper()
'C'
a.upper(c)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    a.upper(c)
TypeError: str.upper() takes no arguments (1 given)
#lower() method
b="PYTHON"
b.lower()
'python'
c="APPLE"
c.lower()
'apple'
#capitalize() method
d="python"
d.capitalize()
'Python'
e="banana"
e.capitalize()
'Banana'
#title() method
f="python is beautiful"
f.title()
'Python Is Beautiful'
g="i love python"
g.title()
'I Love Python'
#isupper(),#islower(),#isdigit(),#isalpha(),#isalnum() methods
a="APPLE"
a.isupper()
True
b="banana"
b.islower()
True
c="12345"
c.isalpha()
False
c.digit()
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    c.digit()
AttributeError: 'str' object has no attribute 'digit'. Did you mean: 'isdigit'?
c.isdigit()
True
d="strawberry"
d.isalpha()
True

e="straw123"
e.isalpha()
False
f="123 456"
f.isdigit()
False
g="apple banana"
g.isalpha()
False
h="grapes123"
h.isalnum()
True
l="grapes 123"
l.isalnum()
False
n=123456
n.isdigit()
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    n.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
#startswith() and #endswith()
q="Computer science"
q.startswith("C")
True
q.startswith("c")
False
w="Hard work"
w.endswith("k")
True
w.endswith("a")
False
#strip()
#lstrip() and rstrip()
t="                     science                              "
t.lstrip()
'science                              '
t.rstrip()
'                     science'
t.strip()
'science'
#split()
a="python java c c++"
a.split()
['python', 'java', 'c', 'c++']
b="i love python"
b.split()
['i', 'love', 'python']
#join()
c="html","css","sql","dsa"
"".join(c)
'htmlcsssqldsa'
" ".join(c)
'html css sql dsa'
d="python java c c++"
" ".join(k)
'N a m e :   H e m a l a t h a \n E m a i l i d :   h e m a @ g m a i l . c o m \t M o b i l e n o :   6 4 5 2 8 4 6 9 2 4 \n C o l l e g e :   V I T W \t B r a n c h :   C S E - D S'
d="python java c c++"
"k".join(d)
SyntaxError: multiple statements found while compiling a single statement
d="python java c c++"
"k".join(d)
'pkyktkhkoknk kjkakvkak kck kck+k+'
e="python","java","html","css"
"g ".join(e)
'pythong javag htmlg css'
f='python java html css'
"v".join(f)
'pvyvtvhvovnv vjvavvvav vhvtvmvlv vcvsvs'
#concatenation()
a="code"
b="gnan"
print(a+b)
codegnan
b="python"
v="course"
print(b+" "+v)
python course
fname="Hema"
lname="muddaraboina"
print(fname+" "+lname)
Hema muddaraboina
#formatting()
a=5
b=6
print(a+b)
11
print("sum is :",a+b)
sum is : 11
city="vijayawada"
print("city is ",city)
city is  vijayawada
#format()
a="hema"
b="latha"
print("hello {} {}".format(a,b))
hello hema latha
print("hello{} hello{}".format(a,b))
hellohema hellolatha
print("hello {} hello {}".format(a,b))
hello hema hello latha
print("hello{}\thello{}".format(a,b))
hellohema	hellolatha
print("hello\t{}\thello\t{}".format(a,b))
hello	hema	hello	latha
print("hello{}\nhello{}".format(a,b))
hellohema
hellolatha
#fstring()
a="hema"
b="latha"
print(f"hello{a} {b}")
hellohema latha
print(f"hello{a} hello{b}")
hellohema hellolatha
print(f"hello {a} hello {b}")
hello hema hello latha
print((f"hello {a} hello {b}").title())
Hello Hema Hello Latha
print(("hello {} hello {}".format(a,b)).title())
Hello Hema Hello Latha
