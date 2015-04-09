
class Processor:
    
    def __init__(self, reader, writer):
        self.reader = reader
        self.writer = writer
        
    def process(self):
        while 1:
            data = self.reader.readline()
            if not data: break
            data = self.convert(data)
            self.writer.write(data)
            
    def convert(self, data):
        assert False, 'convert must be defined'
        
class Uppercase (Processor):
    
    def convert (self, data):
        return data.upper()
    

class HTMLize:
    def write (self, line):
        print ('<PRE>%s</PRE>' % line.rstrip())
        
        
if __name__ == '__main__':
    import sys
    #obj = Uppercase (open('C:\\Users\\sadhikar\\workspace\\LearningPython\\bacon.txt'), sys.stdout)
    obj = Uppercase (open('bacon.txt'), sys.stdout)
    obj.process()
    
    Uppercase (open('bacon.txt'), HTMLize()).process()
        #We get both uppercase conversion (by inheritance) and HTML formatting (by composition)