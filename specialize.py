class Super:
    def method (self):
        print ('in Super.method')

    def delegate (self):
        self.action ()
        
class Inheritor(Super):
    pass

class Replacer (Super):
    def method (self):
        print('in Replacer.method')
        
class Extender (Super):
    def method (self):
        print ('in Extender.method start')
        Super.method(self)
        print ('in Extender.method end')
         
class Provider (Super):
    def action (self):
        print('in Provider.action')
        

if __name__ == '__main__':
    for kl in (Inheritor, Replacer, Extender):
        print('\n' + kl.__name__ + '...')
        kl().method()
    
    print ('\nProvider ...')
    x = Provider()
    x.delegate()