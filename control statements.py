#Control statements
#break
print("------------------break--------------------")
a = 10
while a>1:
    print(a)
    a = a-1
    if a==6 :
        break
print("-----------------------------------")
a = 10
while a>1:
    a = a-1
    if a==6 :
        break
    print(a)
print("-----------------------------------")
for i in range(12):
    if i == 8:
        break
    print(i)
print("-----------------------------------")
for i in range(12):
    print(i)
    if i == 8:
        break
print("-----------------------------------")
a = "python"
for i in a:
    if i == "h":
        break
    print(i)
print("-----------------------------------")
a = "python"
for i in a:
    print(i)
    if i == "h":
        break
print("---------------continue--------------------")
#continue
a = 12
while a>5:
    a = a-1
    if a == 9:
        continue
    print(a)
print("-----------------------------------")
a = 12
while a>5:
    print(a)
    a = a-1
    if a == 9:
        continue
print("-----------------------------------")
for i in range(15):
    if i == 11:
        continue
    print(i)
print("-----------------------------------")
a = "python"
for i in a:
    if i == "h":
        continue
    print(i)
print("----------------------pass-----------------------")
#pass
a = 9
while a > 2:
    print(a)
    a = a - 1
    if a == 7:
        pass
print("-----------------------------------")
for i in range(10):
    if i == 5:
        pass
    print(i)























