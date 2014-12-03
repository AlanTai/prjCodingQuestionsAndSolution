from contextlib import contextmanager

# contextmanager + yield (context manager + generator)
@contextmanager
def run_with(arg):
    print "Start...{0}".format(arg)
    try:
        yield arg + 1
    finally:
        print "End...{0}".format(arg)

# typical way of building with statement
class RunWith():
    def __init__(self, arg):
        self.arg = arg
        
    def __enter__(self):
        print "Start...{0}".format(self.arg)
    def __exit__(self, type, value, traceback):
        print "End...{0}".format(self.arg)
    
if __name__ == "__main__":
    #
    for ith in xrange(10):
        with RunWith(ith):
            print "New Way - Processing...{0}".format(ith)
            
    #
    for jth in xrange(5):
        with run_with(jth):
            print "Typical Way - Processing...{0}".format(jth)
            
            