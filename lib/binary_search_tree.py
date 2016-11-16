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
                self.insert_side("left", current_node, score, movie, depth)
            else:
                self.insert_side("right", current_node, score, movie, depth)

    def insert_side(self, side, current_node, score, movie, depth):
        if side == "left":
            if current_node.left is None:
                current_node.left = n.Node(score, movie)
                return depth
            else:
                self.insert_node(score, movie, current_node.left, depth + 1)
        else:
            if current_node.right is None:
                current_node.right = n.Node(score, movie)
                return depth
            else:
                self.insert_node(score, movie, current_node.right, depth + 1)

    def include(self, score, current_node=None, first_run=True):

        if first_run:
            current_node = self.root

        if current_node is None:
            return False
        else:
            if score == current_node.score():
                return True
            elif score < current_node.score():
                return self.include(score, current_node.left, False)
            else:
                return self.include(score, current_node.right, False)

    def get_depth(self, score, current_node=None, depth=0, first_run=True):
        if first_run:
            current_node = self.root

        if current_node is None:
            return None
        else:
            if score == current_node.score():
                return depth
            elif score < current_node.score():
                return self.get_depth(score, current_node.left, depth + 1, False)
            elif score > current_node.score():
                return self.get_depth(score, current_node.right, depth + 1, False)
