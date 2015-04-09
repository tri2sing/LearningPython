
class Squares:
    
    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop
        
    def __iter__(self):
        #print ('in __iter__')
        return self
    
    def __next__(self):
        #print ('in __next__')
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value ** 2
   

class Iters:
    
    def __init__(self, value):
        self.data = value
    
    def __getitem__(self, i):
        print ('get[%s]' % i, end = ' ')
        return self.data[i]
    
    def __iter__(self):
        print ('iter => ', end = ' ')
        self.ix = 0
        return self
        
    def __next__(self):  
        print ('next => ', end = ' ')
        if self.ix == len(self.data): raise StopIteration
        item = self.data[self.ix]
        self.ix += 1
        return item
    
    def __contains__(self, x):
        print ('contains => ', end = ' ')
        return x in self.data
    
    
if __name__ == '__main__':
    #print ('in main')
    for i in Squares (1, 5):
        print (i, end = ' ')
    print ('\n')

    X = Iters ([1, 2, 3, 4, 5])
    print (3 in X)
    for i in X:
        print (i, end = '  ')
        
    print()
    print ([i**2 for i in X])
    print(list(map(bin, X)))
    
    I = iter(X)
    while True:
        try:
            print(next(I), end = ' @ ')
        except StopIteration:
            break
    