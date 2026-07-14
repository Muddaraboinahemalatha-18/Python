Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #striding
>>> #positive striding
>>> a = "python course"
>>> a[:4]
'pyth'
>>> a[::4]
'pooe'
>>> a[::7]
'pc'
>>> a[: : 7]
'pc'
>>> a[::6]
'p e'
>>> b = "data structures"
>>> b[0:15:2]
'dt tutrs'
>>> b[2:13:3]
'tsuu'
>>> b[4:10:4]
' u'
>>> #negative striding
>>> c = "Machine Learning"
>>> c[::-5]
'ganM'
c[::-3]
'gneehM'
d = "codegnan"
d[-1:-8:-2]
'nneo'
d[-2:10:-3]
''
d[-2:-7:-3]
'ae'
