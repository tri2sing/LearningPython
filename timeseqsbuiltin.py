import sys, mytimer                              # Import timer function
reps = 10000
repslist = range(reps)                           # Hoist range out in 2.6

def forLoop():
    res = []
    for x in repslist:
        res.append(abs(x))
    return res

def listComp():
    return [abs(x) for x in repslist]

def mapCall():
    return list(map(abs, repslist))              # Use list in 3.0 only

def genExpr():
    return list(abs(x) for x in repslist)        # list forces results

def genFunc():
    def gen():
        for x in repslist:
            yield abs(x)
    return list(gen())

print(sys.version)
for test in (forLoop, listComp, mapCall, genExpr, genFunc):
    elapsed, result = mytimer.timer(test)
    print ('-' * 33)
    print ('%-9s: %.5f => [%s...%s]' % (test.__name__, elapsed, result[0], result[-1]))
    
