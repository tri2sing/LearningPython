mystr = 'bacon'
res = list (map(ord, mystr))
print ('The ASCII values for string "' + mystr + '" are:')
print (res)

res1 = [ord(x) for x in mystr]
print (res1)

sqrs1 = [x ** 2 for x in range(10)]
sqrs2 = list(map((lambda x: x ** 2), range(10)))
print (sqrs1)
print (sqrs2)

evns1 = [x for x in range(5) if x % 2 == 0]
evns2 = list(filter((lambda x: x % 2 == 0), range(5)))
print (evns1)
print (evns2)

sqrsevns1 = [x ** 2 for x in range(10) if x % 2 == 0]
sqrsevns2 = list( map((lambda x: x**2), filter((lambda x: x % 2 == 0), range(10))))
print (sqrsevns1)
print (sqrsevns2)

print({x * x for x in range(10)})

print({x: x * x for x in range(10)})

seq1 = 'abc'
seq2 = (1, 2, 3)

l = [(x, y) for x in seq1 for y in seq2]
print (l)

