import time

class Timer(object):
    def __init__(self, verbose=False):
        self.verbose = verbose

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        self.end = time.time()
        self.secs = self.end - self.start
        self.msecs = self.secs * 1000  # millisecs
        if self.verbose:
            print ('elapsed time: %f ms' % self.msecs)


def fibonacci (N):
    if N==0: return 0
    elif N==1: return 1
    else: return fibonacci (N-1) + fibonacci(N-2)
    
if __name__ == '__main__':

    with Timer() as t:
        v = fibonacci(20)
        print(v)
    print ('Elapsed time: %s ms' % t.msecs)
