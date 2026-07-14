Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #list[]
>>> a = [1,2.5,3+5j,"python",True,False]
>>> print(a)
[1, 2.5, (3+5j), 'python', True, False]
>>> type(a)
<class 'list'>
>>> b = 5.5
>>> b
5.5
>>> type(b)
<class 'float'>
>>> c = [7.5]
>>> type(c)
<class 'list'>
>>> #append() method
>>> a = ["python","c","c++"]
>>> a.append("java")
>>> a
['python', 'c', 'c++', 'java']
>>> a.append("html","css")
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a.append("html","css")
TypeError: list.append() takes exactly one argument (2 given)
a.append(["html","css"])
a
['python', 'c', 'c++', 'java', ['html', 'css']]
#extend() method
b = ["html","css","c++"]
b.extend(["python","js"])
b
['html', 'css', 'c++', 'python', 'js']
#insert() method
c = ["vij","hyd","chennai"]
c.insert(1,"vzg")
c
['vij', 'vzg', 'hyd', 'chennai']
c.insert(3,"kerala")
c
['vij', 'vzg', 'hyd', 'kerala', 'chennai']
#index() method
d = ["apple","banana","grapes"]
d.index("grapes")
2
d.index("banana")
1
#copy() method
e = ["bat","boll","wicket"]
e.copy()
['bat', 'boll', 'wicket']
f = e.copy()
f
['bat', 'boll', 'wicket']
#count() method
g = ["apple","banana","grapes"]
g.count("apple")
1
h = ["a","b","c","a","d","a"]
h.count("a")
3
#len() method
i = [1,3,4,5,6,7,2]
len(i)
7
j = ["apple","cherry","strawberry"]
len(j)
3
k = "apple"
len(k)
5
l = ["apple"]
len(l)
1
#pop() method
m = ["bat","boll","wicket"]
m.pop(1)
'boll'
m.pop()
'wicket'
m.pop("bat")
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    m.pop("bat")
TypeError: 'str' object cannot be interpreted as an integer
#remove() method
n = ["apple","mango","kiwi"]
n.remove("mango")
n
['apple', 'kiwi']
n.remove()
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    n.remove()
TypeError: list.remove() takes exactly one argument (0 given)
n.remove(2)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    n.remove(2)
ValueError: list.remove(x): x not in list
n.remove("apple")
n
['kiwi']
#reverse() method
o = [1,3,4,5,6,7,2]
o.reverse()
o
[2, 7, 6, 5, 4, 3, 1]
o = ["blue","black","white","yellow"]
o.reverse()
o
['yellow', 'white', 'black', 'blue']
#clear() method
p = [1,2,3,4,5]
p.clear()
p
[]
p = ["purple","orange","red"]
p.clear()
p
[]
