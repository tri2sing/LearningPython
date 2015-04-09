class Bacon:
    numInstances = 0
    
    def __init__(self):
        Bacon.numInstances += 1
        
    def printNumInstances():
        print('Num of instances = ', Bacon.numInstances)
        
    printNumInstances = staticmethod (printNumInstances) 
     

class Sub (Bacon):
    def printNumInstances():
        print ("Extra Stuff ...")
        Bacon.printNumInstances ()
        
    printNumInstances = staticmethod (printNumInstances)
    
if __name__ == '__main__':
    a = Bacon ()
    b = Bacon ()
    c = Bacon ()
    
    d = Sub ()
    e = Sub ()
    
    
    Bacon.printNumInstances()
    Sub.printNumInstances()
    
    
    