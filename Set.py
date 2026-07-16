Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #set{}
>>> a = {2,3.4,"course",3+5j,True,False}
>>> a
{False, True, 2, 3.4, (3+5j), 'course'}
>>> type(a)
<class 'set'>
>>> b = {2}
>>> type(b)
<class 'set'>
>>> c={7,9,4,7,6,10,20,3}
>>> c
{3, 4, 20, 6, 7, 9, 10}
>>> #add()
>>> d = {3,4,2,5,6,1)
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
>>> d = {3,5,2,6,3,7,1}
>>> d.add(15)
>>> d
{1, 2, 3, 5, 6, 7, 15}
>>> #issubset()
>>> a={3,4,5,6,7,8}
>>> b={6,7,8,9,10}
>>> b.issubset(a)
False
c = {1,2,3}
d = {4,5,6,1,2,3}
c.issubset(d)
True
#superset()
e={5,6,7,8,9,10,11}
f={7,8,9,10}
e.issuperset(f)
True
f.issuperset(e)
False
#union()
a={3,4,5,6,7}
b={1,2,3,4,5,6,7,8}
a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8}
b.union(a)
{1, 2, 3, 4, 5, 6, 7, 8}
#intersection()
t={3,4,5,6,7}
h={1,2,3,4,7,8,9}
t.intersection(h)
{3, 4, 7}
h.intersection(t)
{3, 4, 7}
#difference()
k={7,8,9,10,11,12,13}
l={8,9,10,11,12,13,14,15}
k.difference(l)
{7}
l.difference(k)
{14, 15}
#update()
m={2,3,4,5,6}
n={1,4,5,6,7,8,9}
m.update(n)
m
{1, 2, 3, 4, 5, 6, 7, 8, 9}
n.update(m)
n
{1, 2, 3, 4, 5, 6, 7, 8, 9}
#symmetricdifference()
a={2,3,4,5,6,7,8}
b={1,4,6,8,9,10,11}
a.symmetric_difference(b)
{1, 2, 3, 5, 7, 9, 10, 11}
b.symmetric_difference(a)
{1, 2, 3, 5, 7, 9, 10, 11}
#difference_update()
v = {1,3,4,2}
k = {4,5,3,5,6,7}
v.difference_update(k)
v
{1, 2}
k.difference_update(v)
k
{3, 4, 5, 6, 7}
#intersection_update()
a={3,4,5,6,7,8}
b={5,6,7,8,9,10}
a.intersection_update(b)
a
{8, 5, 6, 7}
b.intersection_update(a)
b
{8, 5, 6, 7}
#symmetric_update()
#symmetric_difference_update()
c={11,12,13,14,15,16}
d={13,14,15,16,17,18}
c.symmetric_difference_update(d)
c
{17, 18, 11, 12}
d.symmetric_difference_update(c)
d
{16, 11, 12, 13, 14, 15}
#copy()
v = {1,3,4,3,5,6,7}
h = v.copy()
v
{1, 3, 4, 5, 6, 7}
h
{1, 3, 4, 5, 6, 7}
#discard()
numbers = {1, 2, 3, 4}
numbers.discard(3)
numbers
{1, 2, 4}
numbers.discard(10)
numbers
{1, 2, 4}
#remove()
letters = {"a", "b", "c"}
letters.remove("b")
letters
{'a', 'c'}
letters.remove("z")
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    letters.remove("z")
KeyError: 'z'
#isdisjoint()
set1 = {1, 2, 3}
set2 = {4, 5, 6}
set3 = {3, 7, 8}
print(set1.isdisjoint(set2))
True
print(set1.isdisjoint(set3))
False
print(set2.isdisjoint(set3))
True
#pop()
a={3,4,5,6,7,8}
a,pop()
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    a,pop()
NameError: name 'pop' is not defined. Did you mean: 'pow'?
a.pop()
3
a.pop()
4
a.pop(5)
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    a.pop(5)
TypeError: set.pop() takes no arguments (1 given)
#clear()
v={3,4,5,6,7,8}
v.clear()
v
set()
t = {18,12,25,30,95}
t.clear()
t
set()
