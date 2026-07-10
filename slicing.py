Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #Slicing
>>> #Positive
>>> a="work until you succeed"
>>> a[0:4]
'work'
>>> a[5:10]
'until'
>>> a[15:22]
'succeed'
>>> a[5:14]
'until you'
>>> b="Time is very precious"
>>> b[0:4]
'Time'
>>> b[8:12]
'very'
>>> b[13:21]
'precious'
>>> #Negative
>>> c="simple is better than complex"
>>> c[-19:-13]
'better'
>>> c[-29:-23]
'simple'
c[-7:]
'complex'
d="codegnan IT solutions"
d[-21:-13]
'codegnan'
d[-9:0]
''
d[-9:-1]
'solution'
d[-9:]
'solutions'
