def echo (message):
    print (message)
    
echo ('Direct Call')

X = echo

X ('Indirect Call')

def indirect(func, arg):
    func (arg)
    
indirect (echo, 'Argument Call')

schedule = [ (echo, 'Bacon!'), (echo, 'Eggs!') ]
for (func, arg) in schedule:
    func (arg)
    
def make (label):
    def made_echo (message):
        print (label + ': ' + message)
    return made_echo

F = make ('Bacon')
F('Eggs')

lamf = lambda x, y, z: x+y+z

print (lamf (2, 3, 4))
print (lamf ('Breakfast = ', 'Bacon + ', 'Eggs'))
