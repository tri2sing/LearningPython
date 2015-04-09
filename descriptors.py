
class Name:

    "Descriptor Name that intercept calls to an attribute"

    def __get__(self, instance, owner):
        print('get ...')
        return instance._attr
    
    def __set__ (self, instance, value):
        print('set ...')
        instance._attr = value
        return
    
    def __delete__(self, instance):
        print('delete ...')
        del instance._attr
        return
    
    
class Person:
    
    def __init__(self, name):
        self.name = name
        return

    name = Name()   # Attaching to the descriptor
    
    
bob = Person('Bob Smith')
print(bob.name)
bob.name = 'Robert Smith'
print(bob.name)
del bob.name

print('-'*25)
sue = Person('Sue Jones')
print(sue.name)
print(Name.__doc__)


class DescSquare:
    
    def __init__(self, start):
        self.value = start
        return
    
    def __get__(self, instance, owner):
        return self.value**2
    
    def __set__(self, instance, value):
        self.value = value
    
        
class Client1:
    X = DescSquare(3)
    
    
class Client2:
    X = DescSquare(32)
    
    
c1 = Client1()
c2 = Client2()

print('-'*25)
print(c1.X)
c1.X = 4
print(c1.X)
print(c2.X)

print('-'*25)


class DescState:
    
    def __init__(self, value):
        self.value = value
        
    def __get__(self, instance, owner):
        print('DescState get')
        return self.value*10
    
    def __set__(self, instance, value):
        print('DescState set')
        self.value = value
        

class CalcAttrs:
    
    X = DescState(2)    # Class attribute attached to descriptor class
    Y = 3               # Class attribute
    
    def __init__(self):
        self.Z = 4      # Instance attribute 
        

obj = CalcAttrs()
print(obj.X, obj.Y, obj.Z)
obj.X = 5
obj.Y = 6
obj.Z = 7
print(obj.X, obj.Y, obj.Z)

print('-'*25)

class InstState:                           # Using instance state
    def __get__(self, instance, owner):
        print('InstState get')             # Assume client class instance has attribute _Y
        return instance._Y * 100
    def __set__(self, instance, value):
        print('InstState set')
        instance._Y = value

# Client class

class CalcAttrs2:
    X = DescState(3)                       # Descriptor attached to class attribute
    Y = InstState()                        # Descriptor attached to class attribute
    def __init__(self):
        self._Y = 3                        # Instance attribute
        self.Z  = 4                        # Instance attribute

obj = CalcAttrs2()
print(obj.X, obj.Y, obj.Z)                 # X and Y are computed, Z is not
obj.X = 5                                  # X and Y assignments intercepted
obj.Y = 6
obj.Z = 7        
print(obj.X, obj.Y, obj.Z)
        

        