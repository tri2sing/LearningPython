class C: pass

i = C()
print (type(i))             # Type of instance is class it's made from
print(i.__class__)
print (type(C))             # Class is a type, and type is a class
print(C.__class__)
print (type([1, 2, 3]))     # Classes and built-in types work the same
print (type(list))
print(list.__class__)


