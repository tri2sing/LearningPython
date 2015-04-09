
def gensquares(N):
    for i in range(N):
        yield(i**2)

for i in gensquares(5):
    print (i, end = ': ')
    
print('\n')

ge = (x**2 for x in range(4))
print(next(ge))
print(next(ge))
print(next(ge))
print(next(ge))

print(sum(x**3 for x in range(4)))

print(sorted(x**3 for x in range(4)))

print(sorted((x**3 for x in range(4)), reverse=True))

import math

print(list(map(math.sqrt, (x**2 for x in range(4)))))


def counter(maximum):
    i = 0
    while i < maximum:
        print ('Current value of i = ' + str(i))
        val = (yield i)
        # If value provided, change counter
        if val is not None:
            print ('val is not None')
            i = val
        else:
            print ('val is None')
            i += 1

it = counter (10)
print ('Calling next - 1')
print(next (it))
print ('Calling next - 2')
print(next (it))
print ('Calling send - 3')
it.send(7)
print ('Calling next - 4')
print(next (it))
print ('Calling next - 5')
print(next (it))



