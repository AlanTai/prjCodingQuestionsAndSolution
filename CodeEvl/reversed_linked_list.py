'''
Created on Oct 22, 2014

@author: alantai
'''

class Node():
    def __init__(self, arg_node_str = "default string"):
        self.node_str = arg_node_str
        self.next_node = None
        
class LinkedList():
    def __init__(self):
        self.root = None
        
    def add_node(self, arg_node = None):
        if not arg_node:
            return "Please give a valid Node object"
            
        if not self.root:
            self.root = arg_node
        else:
            current_node = self.root
            while current_node.next_node:
                current_node = current_node.next_node
            current_node.next_node = arg_node

class Stack(object):
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
    
    def put(self, arg_item):
        self.items.append(arg_item)
        
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items) - 1]
    
    def size(self):
        return len(self.items)
        
if __name__ == "__main__":
    node_1 = Node(arg_node_str = "first node")
    node_2 = Node(arg_node_str = "second node")
    node_3 = Node(arg_node_str = "third node")
    
    linked_list = LinkedList()
    linked_list.add_node(node_1)
    linked_list.add_node(node_2)
    linked_list.add_node(node_3)
    
    my_stack = Stack()
    current_node = linked_list.root
    while current_node:
        print current_node.node_str
        my_stack.put(current_node)
        current_node = current_node.next_node
    print "=================================="
    
    linked_list = LinkedList()
    while not my_stack.isEmpty():
        new_node = my_stack.pop()
        if new_node:
            new_node.next_node = None
            linked_list.add_node(new_node)
        
    
    current_node = linked_list.root
    while current_node:
        print current_node.node_str
        current_node = current_node.next_node
    print "=================================="