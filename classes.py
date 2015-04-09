class FirstClass():
    
    def setdata (self, value):
        self.data = value
        
    def display(self):
        print (self.data)

class SecondClass(FirstClass):
    
    def display (self):
        print('Current value = "%s"' % self.data)

class ThirdClass (SecondClass):
    
    def __init__ (self, value):
        self.data = value
        
    def __add__ (self, other):
        return ThirdClass (self.data + other)
    
    def __str__ (self):
        return '[ThirdClass: %s]' % self.data
    
    def mul (self, other):
        self.data *= other

class MixedNames ():
    data = 'spam'
    
    def __init__(self, value):
        self.data = value
        
    def display (self):
        print (self.data, MixedNames.data)
        
    
if __name__ == "__main__":
    
    x = FirstClass()
    y = FirstClass()
      
    x.setdata ('Sameer')
    y.setdata (3.14159)
    
    x.display()
    
    z = SecondClass()
    z.setdata (42)
    z.display()
    
    y.display()  
    
    a = ThirdClass ('abc')
    a.display ()
    print (a)
    b = a + 'xyz'
    print (b)
    a.mul (3)
    print (a)
    
    mn1 = MixedNames(1)
    mn2 = MixedNames(2)
    mn1.display ()
    mn2.display ()
    
    