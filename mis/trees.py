# We could represent that tree with lists of lists, like this
T = [["a", "b"], ["c"], ["d", ["e", "f"]]]

class Tree:
def __init__(self, left, right): self.left = left
    self.right = right