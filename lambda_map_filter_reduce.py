# The following lambdas work in the interactive console.  
# But not when imported from a file.  
# Get a not defined when trying to call lambda after import.
# Actually they work.
# The issue is that PyDev does not flush the output to the console immediately.
 
f = lambda x, y, z: x + y + z
print(f(2, 3, 4))

x = (lambda a = 'fee', b = 'fie', c = 'foe': a + ': ' + b + ': ' + c)
print(x('wee'))

def knights ():
    title = 'Sir'
    action = (lambda x: title + ' ' + x)
    return action

act = knights ()
print(act ('Robin'))

L = [
     lambda x: x**2,
     lambda x: x**3,
     lambda x: x**4
    ]

for f in L:
    print(f(2))
    
print (L[0](3))

lower = (lambda x, y: x if x < y else y)
print (lower ('aa', 'bb'))
print (lower (5, 3))

counters = [1, 2, 3, 4]
print(list (map(lambda x: x + 10, counters)))

print(list(map(pow, [1, 2, 3], [2, 3, 4])))

print(list (filter(lambda x: x>0, range(-5, 5))))
print(list (map(lambda x: x>0, range(-5, 5))))

from functools import reduce

print(reduce((lambda x, y: x + y), [1, 2, 3, 4]))
print(reduce((lambda x, y: x * y), [1, 2, 3, 4]))


