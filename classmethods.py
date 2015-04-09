class Bacon:
    numInstances = 0
    
    def __init__(self):
        Bacon.numInstances += 1
        
    def printNumInstances(cls):
        print('Num of instances = ', cls.numInstances)
        
    printNumInstances = classmethod (printNumInstances) 
     

class Sub (Bacon):
    def printNumInstances(cls):
        print ("Extra Stuff ...")
        Bacon.printNumInstances ()
        
    printNumInstances = classmethod (printNumInstances)
    
if __name__ == '__main__':
    a = Bacon ()
    b = Bacon ()
    c = Bacon ()
    
    d = Sub ()
    e = Sub ()
    
    
    Bacon.printNumInstances()
    Sub.printNumInstances()
    
    
    