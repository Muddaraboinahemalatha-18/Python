Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #tuple()
>>> a = (3,4.5,5+3j,"python",True,False)
>>> a
(3, 4.5, (5+3j), 'python', True, False)
>>> type(a)
<class 'tuple'>
>>> b = (3)
>>> type(b)
<class 'int'>
>>> c = (4,)
>>> type(c)
<class 'tuple'>
>>> #index() method
>>> d = (3,4.5,5+3j,"python",True,False)
>>> d.index(True)
4
>>> d.index("python")
3
>>> #len() method
>>> e = (4,3.6,"code","course",True)
>>> len(e)
5
>>> f = (3,17,4,33,73)
len(f)
5
#count() method
g = (3,2,5,6,3,7)
g.count(3)
2
h = ("code","course","code","python")
h.count("code")
2
#max() method
i = (77,35,54,12,3,84,93,2,1)
max(i)
93
#min() method
j = (77,35,54,12,3,84,93,2,1)
min(j)
1
#sum() method
k = (77,35,54,12,3,84,93,2,1)
sum(k)
361
#sorted() method
l = (3,5,102,45,73,2,65,203,355,25)
sorted(l)
[2, 3, 5, 25, 45, 65, 73, 102, 203, 355]
