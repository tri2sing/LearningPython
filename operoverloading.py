class Commuter:
    
    def __init__(self, val):
        self.val = val
    
    def __add__(self, other): # __add__ can get called when other is or is not of type Commuter
        print ('add', self.val, other)
        if isinstance (other, Commuter):
            other = other.val
        return Commuter(self.val + other) # We return a Commuter object to ensure that commutative addition expression work
        
    def __radd__(self, other):  #__radd__ is called when other is not of type Commuter
        print ('radd', self.val, other)
        return Commuter(other + self.val)
    
    def __str__(self):
        return '<Commuter" %s>' % self.val
 
class Callee:
    
    def __call__(self, *pargs, **kargs):
        print ('Called: ', pargs, kargs)
        
            
if __name__ == '__main__':
    x = Commuter (88)
    y = Commuter (89)
    
    print(x+10)      # __add__ gets called
    print (10+y)     # __radd__ gets called
    z = x + y
    print (z)      
    print (z+10)
    print (z+z)     
    
    C = Callee()
    C(1, 2, 3)
    C(1, 2, 3, x=4, y=5)
    
