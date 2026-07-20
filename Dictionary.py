Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> # Dictionary
>>> student = {"name": "Alice", "age": 21, "course": "Python"}
>>> print(student)
{'name': 'Alice', 'age': 21, 'course': 'Python'}
>>> type(student)
<class 'dict'>
>>> student = {"name": "Alice", "age": 21, "course": "Python"}
>>> print(student["name"])
Alice
>>> print(student.get("age"))
21
>>> #Adding items
>>> student = {"name": "latha", "age": 21, "course": "Python"}
>>> student["grade"] = "A"
>>> student["age"] = 22
>>> print(student)
{'name': 'latha', 'age': 22, 'course': 'Python', 'grade': 'A'}
>>> #Checking Existence
>>> print("name" in student)
True
>>> print("grade" not in student)
False
>>> #Methods in dictionary
>>> #keys()
student = {"name": "hema", "age": 21, "course": "Python"}
print(student.keys())
dict_keys(['name', 'age', 'course'])
#values()
student = {"name": "hema", "age": 21, "course": "Python"}
print(student.values())
dict_values(['hema', 21, 'Python'])
#items()
student = {"name": "hema", "age": 21, "course": "Python"}
print(student.items())
dict_items([('name', 'hema'), ('age', 21), ('course', 'Python')])
#get(key)
college = {"branch":"CSE","rollno":4425,"year":2022}
print(college.get("year"))
2022
#get(key, default)
college = {"branch":"CSE","rollno":4425,"year":2022}
print(college.get("aadharno"))
None
print(college.get("aadhar", "N/A"))
N/A
#update()
college = {"branch":"CSE","rollno":4425,"year":2022}
college.update({"age": 22, "city": "Delhi"})
print(college)
{'branch': 'CSE', 'rollno': 4425, 'year': 2022, 'age': 22, 'city': 'Delhi'}
#pop(key)
college = {"branch":"CSE","rollno":4425,"year":2022}
removed = course.pop("year")
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    removed = course.pop("year")
NameError: name 'course' is not defined
removed = college.pop("year")
print(removed)
2022
print(college)
{'branch': 'CSE', 'rollno': 4425}
#popitem()
college = {'branch': 'CSE', 'rollno': 4425, 'year': 2022, 'age': 22, 'city': 'Delhi'}
last_item = college.popitem()
print(last_item)
('city', 'Delhi')
last_item = college.popitem()
print(last_item)
('age', 22)
print(college)
{'branch': 'CSE', 'rollno': 4425, 'year': 2022}
#
KeyboardInterrupt
#clear()
college.clear()
print(college)
{}
#copy()
student = {"name": "Alice", "age": 21}
v = student.copy()
print(v)
{'name': 'Alice', 'age': 21}
#setdefault(key, default)
student = {"name": "Alice", "age": 21}
student.setdefault("grade", "A")
'A'
print(student)
{'name': 'Alice', 'age': 21, 'grade': 'A'}
#fromkeys(keys, value)
keys = ["a", "b", "c"]
new_dict = dict.fromkeys(keys, 0)
print(new_dict)
{'a': 0, 'b': 0, 'c': 0}
#Dictionary does not allow duplicates
my_dict = {"a": 10, "b": 20, "c": 10, "a": 30}
print(my_dict)
{'a': 30, 'b': 20, 'c': 10}
my_dict = {"a": 10, "b": 20, "c": 10, "a": 10}
print(my_dict)
{'a': 10, 'b': 20, 'c': 10}
my_dict = {"a": 10, "b": 20, "c": 10, "a1": 10}
print(my_dict)
{'a': 10, 'b': 20, 'c': 10, 'a1': 10}
