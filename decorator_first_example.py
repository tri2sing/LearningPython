
class tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func
        print ('__init_ called for %s' % self.__class__.__name__)
    
    def __call__(self, *args):
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        self.func(*args)
        
@tracer
def bacon (a, b, c):
    print (a, b, c)
    
bacon(1, 2, 3)
bacon('a', 'b', 'c')
bacon(4, 5, 6)
        