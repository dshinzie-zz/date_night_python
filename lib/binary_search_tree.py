from pdb import set_trace as bp
import sys
sys.path.append('/Users/danielshin/Documents/turing/other/python/date_night_python/lib')
import node as n

class BinarySearchTree:
    def __init__(self, root=None, sorted=[]):
        self.root = root
        self.sorted = sorted
        self.healh = []

    def insert_node(self, score, movie, current_node=None, depth=1):
        if current_node is None:
            current_node = self.root

        if self.root is None:
            self.root = n.Node(score, movie)
            return 0

        else:
            if score == current_node.score():
                return None
            if score < current_node.score():
                if current_node.left is None:
                    current_node.left = n.Node(score, movie)
                    return depth
                else:
                    self.insert_node(score, movie, current_node.left, depth+1)
            else:
                if current_node.right is None:
                    current_node.right = n.Node(score, movie)
                    return depth
                else:
                    self.insert_node(score, movie, current_node.right, depth+1)
