# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import unittest
import sys
sys.path.append('/Users/danielshin/Documents/turing/other/python/date_night_python/lib')

import binary_search_tree as bs

class BinarySearchTreeTest(unittest.TestCase):

    def test_root_node_is_inserted(self):
        tree =  bs.BinarySearchTree()
        tree.insert_node(100, "Test Movie")

        self.assertEqual(tree.root.score(), 100)

    def test_node_alrady_exists(self):
        tree =  bs.BinarySearchTree()
        tree.insert_node(100, "Test Movie")

        self.assertEqual(tree.insert_node(100, "Test Movie"), None)

    def test_insert_left_node(self):
        tree =  bs.BinarySearchTree()
        tree.insert_node(100, "Test Movie")
        tree.insert_node(50, "Test Movie 2")

        self.assertEqual(tree.root.left.score(), 50)

    def test_insert_multiple_left(self):
        tree =  bs.BinarySearchTree()
        tree.insert_node(100, "Test Movie")
        tree.insert_node(50, "Test Movie 2")
        tree.insert_node(25, "Test Movie 3")
        tree.insert_node(10, "Test Movie 4")

        self.assertEqual(tree.root.left.score(), 50)
        self.assertEqual(tree.root.left.left.score(), 25)
        self.assertEqual(tree.root.left.left.left.score(), 10)

    def test_insert_right_node(self):
        tree =  bs.BinarySearchTree()
        tree.insert_node(50, "Test Movie")
        tree.insert_node(75, "Test Movie 2")

        self.assertEqual(tree.root.right.score(), 75)

    def test_insert_multiple_right(self):
        tree =  bs.BinarySearchTree()
        tree.insert_node(50, "Test Movie")
        tree.insert_node(60, "Test Movie 2")
        tree.insert_node(70, "Test Movie 3")
        tree.insert_node(80, "Test Movie 4")

        self.assertEqual(tree.root.right.score(), 60)
        self.assertEqual(tree.root.right.right.score(), 70)
        self.assertEqual(tree.root.right.right.right.score(), 80)

    def test_left_and_right(self):
        tree =  bs.BinarySearchTree()
        tree.insert_node(50, "Test Movie")
        tree.insert_node(25, "Test Movie 2")
        tree.insert_node(75, "Test Movie 3")
        tree.insert_node(35, "Test Movie 4")
        tree.insert_node(65, "Test Movie 5")

        self.assertEqual(tree.root.left.score(), 25)
        self.assertEqual(tree.root.right.score(), 75)
        self.assertEqual(tree.root.left.right.score(), 35)
        self.assertEqual(tree.root.right.left.score(), 65)

    def test_returns_none_if_same_score(self):
        tree = bs.BinarySearchTree()
        tree.insert_node(50, "Test Movie")
        tree.insert_node(25, "Test Movie 2")

        self.assertEqual(tree.insert_node(50, "Test Movie 3"), None)
        self.assertEqual(tree.insert_node(25, "Test Movie 4"), None)

    def test_tree_includes_score(self):
        tree = bs.BinarySearchTree()
        tree.insert_node(50, "Test Movie")
        tree.insert_node(25, "Test Movie 2")

        self.assertEqual(tree.include(50), True)
        self.assertEqual(tree.include(25), True)
        self.assertEqual(tree.include(10), False)

    def test_tree_shows_depth(self):
        tree = bs.BinarySearchTree()
        tree.insert_node(50, "Test Movie")

        self.assertEqual(tree.get_depth(50), 0)

    def test_tree_shows_multiple_depths(self):
        tree = bs.BinarySearchTree()
        tree.insert_node(50, "Test Movie")
        tree.insert_node(25, "Test Movie 2")
        tree.insert_node(100, "Test Movie 3")
        tree.insert_node(35, "Test Movie 4")
        tree.insert_node(30, "Test Movie 5")

        self.assertEqual(tree.get_depth(50), 0)
        self.assertEqual(tree.get_depth(25), 1)
        self.assertEqual(tree.get_depth(100), 1)
        self.assertEqual(tree.get_depth(35), 2)
        self.assertEqual(tree.get_depth(30), 3)


if __name__ == '__main__':
    unittest.main()
