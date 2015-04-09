X = 11 # Global module name

def f():
    print (X)
    
def g():
    X = 22 # local function name, hides global module name
    print (X)
    
class C:
    X = 33 # class attribute
    
    def m(self):
        X = 44 # local method variable
        X += 1
        self.X = 55 # instance attribute

if __name__ == '__main__':
    print(X) # 11: module
    f() # 11: global
    g() # 22: local
    print(X) # 11: module name unchanged
    
    obj = C()
    print(obj.X) # 33: class name inherited by instance
    
    obj.m() # attach attribute X to instance
    print(obj.X) # 55: instance

    print (C.X) # 33: class 
    