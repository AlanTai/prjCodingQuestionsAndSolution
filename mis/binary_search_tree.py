class Node(object):
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None
        
    def __str__(self):
        return str(self.info)
        
class SearchTree(object):
    def __init__(self):
        self.roor = None
        
    def create(self, val):
        if self.root == None:
            self.root = Node(val)
            
        else:
            current =self.root
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                        
                    elif val > current.info:
                        if current.right:
                            current = current.right
                        else:
                            current.right = Node(val)
                            break
                    else:
                        break
                        
    def in_order(self, node):
        if node is not None:
            self.in_order(node.left)
            print node.info
            self.in_order(node.right)