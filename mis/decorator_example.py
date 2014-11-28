# decoraotr example; decorator is a way of passing a function as a callback into another function and, after processing, return the callback function

def logger(func):
    def inner(*args, **kwargs):
        print "Arguments were: {0} ; {1}".format(args, kwargs)
        return func(*args, **kwargs)
    return inner
    
    
@logger
def test_1(*args, **kwargs):
    return "Var: {0}, {1}".format(args, kwargs)
    
if __name__ == "__main__":
    _dict = {'_x' : 1, '_y' : 1}
    print test_1(2, 9, **_dict)