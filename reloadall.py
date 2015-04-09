"""
reloadall.py: transitively reload nested modules
"""

import types
from imp import reload                               # from required in 3.0

def status(module):
    print('reloading ' + module.__name__)

def transitive_reload(module, visited):
    if not module in visited:                        # Trap cycles, duplicates
        status(module)                               # Reload this module
        if '__loader__' in module.__dict__:         # Sameer: builtins does not have an attribute __loader__
                                                    # If a module does not have __loader__ then the reload function fails.
            reload(module)                               # And visit children
        visited[module] = None
        for attrobj in module.__dict__.values():     # For all attrs
            if type(attrobj) == types.ModuleType:    # Recur if module
                print ('Child is: ' + attrobj.__name__)
                transitive_reload(attrobj, visited)

def reload_all(*args):
    visited = {}
    for arg in args:
        if type(arg) == types.ModuleType:
            transitive_reload(arg, visited)

if __name__ == '__main__':
    import reloadall                                 # Test code: reload myself
    reload_all(reloadall)                            # Should reload this, types
    
