'''
Created on Oct 27, 2014

@author: alantai

@Note: Sorted linked list can be used for solving skyline problem
'''
class Node(object):
    def __init__(self, arg_node_value = None):
        self.node_value = arg_node_value
        self.next_node = None
        
class SortedLinkedList(object):
    def __init__(self):
        self.root = None
        
    def add_node(self, arg_node = None):
        if not arg_node:
            return "Please give a valid node"
        
        if not self.root:
            self.root = arg_node
        else:
            current_node = self.root
            previous_node = None
            
            while True:
                if arg_node.node_value < current_node.node_value:
                    if previous_node:
                        previous_node.next_node = arg_node
                        arg_node.next_node = current_node
                    else:
                        arg_node.next_node = current_node
                        self.root = arg_node
                    break
                else:
                    if current_node.next_node:
                        previous_node = current_node
                        current_node = current_node.next_node
                    else:
                        current_node.next_node = arg_node
                        break
                    
if __name__ == "__main__":
    node_1 = Node(2)
    node_2 = Node(9)
    node_3 = Node(0)
    node_4 = Node(4)
    node_5 = Node(3)
                    
    sorted_linked_list = SortedLinkedList()
    sorted_linked_list.add_node(node_1)
    sorted_linked_list.add_node(node_2)
    sorted_linked_list.add_node(node_3)
    sorted_linked_list.add_node(node_4)
    sorted_linked_list.add_node(node_5)
                    
    current_node = sorted_linked_list.root
    while True:
        print current_node.node_value
        
        if not current_node.next_node:
            break
        else:
            current_node = current_node.next_node