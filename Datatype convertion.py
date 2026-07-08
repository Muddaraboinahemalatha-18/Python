Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Datatype Convertion
# convert to int
int(5)
5
int(7.2)
7
int("apple")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int("apple")
ValueError: invalid literal for int() with base 10: 'apple'
int(3+5j)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int(3+5j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
int(False)
0
#convert to float
float(5)
5.0
float(12.3)
12.3
float("banana")
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    float("banana")
ValueError: could not convert string to float: 'banana'
float(2+7j)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    float(2+7j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
1.0
float(False)
0.0
#convert to str()
str(5)
'5'
str(2.3)
'2.3'
str("python")
'python'
str(1+2j)
'(1+2j)'
str(True)
'True'
str(False)
'False'
#convert to complex
complex(8)
(8+0j)
complex(7.5)
(7.5+0j)
>>> complex("berries")
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    complex("berries")
ValueError: complex() arg is a malformed string
>>> complex(95+5j)
(95+5j)
>>> complex(True)
(1+0j)
>>> complex(False)
0j
>>> #convert to bool
>>> bool(7)
True
>>> bool(8.5)
True
>>> bool("strawberry")
True
>>> bool(5+7j)
True
>>> bool(True)
True
>>> bool(False)
False
