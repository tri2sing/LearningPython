
class ListInstance:
    
    def __str__(self):
        return '<Instance of %s, address of %s:\n%s' % (self.__class__.__name__, id(self), self.__attrnames())
    
    # pseudo-private name for the method
    def __attrnames(self):
        result = ''
#        for attr in sorted(self.__dict__):
#            result += '\tname %s = %s\n' % (attr, self.__dict__[attr])
        for attr in dir(self):
            if attr[:2] == '__' and attr[-2:] == '__':
                result += '\tname %s = <>\n' % attr
            else:
                result += '\tname %s = %s\n' % (attr, getattr(self,attr))
                
        return result

class ListTree:
    
    def __str__(self):
        self.__visited = {}
        return '<Instance of {0}, address {1}:\n{2}{3}>'.format(self.__class__.__name__, id(self), self.__attrnames(self, 0), self.__listclass(self.__class__, 4))
    
    def __listclass(self, aClass, indent):
        dots = '.' * indent
        if aClass in self.__visited:
            return '\n{0}<Class {1}:, address {2}: (see above)>\n'.format(dots, aClass.__name__, id(aClass))
        else:
            self.__visited[aClass] = True
            genabove = (self.__listclass(c, indent+4) for c in aClass.__bases__)
            return '\n{0}<Class {1}, address {2}:\n{3}{4}{5}>\n'.format(dots, aClass.__name__, id(aClass), self.__attrnames(aClass, indent), ''.join(genabove), dots)

    def __attrnames(self, obj, indent):
        spaces = ' ' * (indent + 4)
        result = ''
        for attr in sorted(obj.__dict__):
            if attr.startswith('__') and attr.endswith('__'):
                result += spaces + '{0}=<>\n'.format(attr)
            else:
                result += spaces + '{0}={1}\n'.format(attr, getattr(obj, attr))
        return result
    
        
if __name__ == '__main__':
    
    class Bacon (ListInstance):
        def __init__(self, data):
            self.data = data
        
        def hello (self):
            pass
        
    x = Bacon ('yummy')
    print (x)
    

    class Salami (ListTree):
        def __init__(self, data):
            self.data = data
        
        def hello (self):
            pass
        
    x = Salami ('yummy too')
    print (x)
    