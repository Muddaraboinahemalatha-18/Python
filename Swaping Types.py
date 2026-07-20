#Swaping Types
# 1 swaping of two numbers using without third variable
a = 10
b = 20
a,b = b,a
print("a value is:",a)
print("b value is:",b)
print("-----------------------------------")
#2 swaping of two numbers using third variable
c = 10
d = 20
temp = c
c = d
d = temp
print("c value is:",c)
print("d value is:",d)
print("-----------------------------------")
#3 swaping of two numbers using arthematic operators
e = 10
f = 20
e=e+f
f=e-f
e=e-f
print("e value is:",e)
print("f value is:",f)
print("-----------------------------------")
#4 swaping of two numbers using numbering formate
g=10
h=20
print("After swaping: g=%d, h=%d" %(h,g))
print("After swaping: g=%f, h=%f" %(h,g))
print("After swaping: g=%.2f, h=%.2f" %(h,g))

