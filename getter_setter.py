# -*- ccoding: utf-8 -*-
class MyClass(object):
    def __init__(self):
        self._x = None
        
    @property
    def x(self):
        return self._x
        
    @x.setter
    def x(self, value):
        self._x = value
        
    @x.deleter
    def x(self):
        del self._x
        
if __name__ == "__main__":
    new_item = MyClass()
    new_item.x = "hello"
    
    print new_item.x
    del(new_item.x)