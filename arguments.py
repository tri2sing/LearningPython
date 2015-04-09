# from imp import reload

def f(a):
    a = 99
    print ('a = ', a)
    
b = 88
print ('b = ', b)
f (b)
print ('b = ', b)

def changer (a, b):
    a = 2
    b[0] = 'bacon'
    print (a, b)
    
x = 1
l = [1, 2]
print ('x = ', x, '; l = ', l)
changer (x, l)
print ('x = ', x, '; l = ', l)

def arbitpos (*pargs): 
    print (pargs)

arbitpos()
arbitpos(1)
arbitpos(1, 2, 3)

def arbitkey (**kwargs):
    print (kwargs)
    
arbitkey()
arbitkey (a=1, b=2)

def arbittotal (a, *posargs, **kwargs):
    print(a, posargs, kwargs)
    
arbittotal (1)
arbittotal (1, 2)
arbittotal (1, 2, 3, x=1, y=2)

def unpack (a, b, c, d):
    print (a, b, c, d)

pargs = (1, 2)
pargs += (3, 4)
unpack (*pargs)

kargs = {'a': 5, 'b': 6, 'c': 7}
kargs['d'] = 8
unpack (**kargs)

unpack(*(11, 12), **{'d': 13, 'c': 14})
unpack(21, *(22, 23), **{'d': 24}) 
unpack (31, *(32, 33), d=34)
unpack(41, *(42,), c=43, **{'d':44})    

def kwonly (a, *b, c):
    print (a, b, c)

kwonly (1, 2, c=3)
kwonly (11, c=13)

