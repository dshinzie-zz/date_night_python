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

        self.assertEqual(tree.depth_of(50), 0)

    def test_tree_shows_multiple_depths(self):
        tree = bs.BinarySearchTree()
        tree.insert_node(50, "Test Movie")
        tree.insert_node(25, "Test Movie 2")
        tree.insert_node(100, "Test Movie 3")
        tree.insert_node(35, "Test Movie 4")
        tree.insert_node(30, "Test Movie 5")

        self.assertEqual(tree.depth_of(50), 0)
        self.assertEqual(tree.depth_of(25), 1)
        self.assertEqual(tree.depth_of(100), 1)
        self.assertEqual(tree.depth_of(35), 2)
        self.assertEqual(tree.depth_of(30), 3)

    def test_tree_returns_max(self):
        tree = bs.BinarySearchTree()
        tree.insert_node(50, "Test Movie")
        tree.insert_node(25, "Test Movie 2")

        self.assertEqual(tree.max(), { "Test Movie": 50 })

    def test_tree_returns_max_multiple(self):
        tree = bs.BinarySearchTree()
        tree.insert_node(50, "Test Movie")
        tree.insert_node(25, "Test Movie 2")
        tree.insert_node(100, "Test Movie 3")
        tree.insert_node(35, "Test Movie 4")
        tree.insert_node(30, "Test Movie 5")

        self.assertEqual(tree.max(), { "Test Movie 3": 100 })

    def test_tree_returns_min(self):
        tree = bs.BinarySearchTree()
        tree.insert_node(50, "Test Movie")
        tree.insert_node(25, "Test Movie 2")

        self.assertEqual(tree.min(), { "Test Movie 2": 25 })

    def test_tree_returns_min_multiple(self):
        tree = bs.BinarySearchTree()
        tree.insert_node(50, "Test Movie")
        tree.insert_node(25, "Test Movie 2")
        tree.insert_node(100, "Test Movie 3")
        tree.insert_node(35, "Test Movie 4")
        tree.insert_node(30, "Test Movie 5")

        self.assertEqual(tree.min(), { "Test Movie 2": 25 })

    def test_tree_sorts_left(self):
        tree = bs.BinarySearchTree()
        tree.insert_node(50, "Test Movie")
        tree.insert_node(25, "Test Movie 2")
        expected = [{"Test Movie 2": 25}, {"Test Movie": 50}]

        self.assertEqual(tree.sort(), expected)

    def test_tree_sorts_right(self):
        tree = bs.BinarySearchTree()
        tree.insert_node(50, "Test Movie")
        tree.insert_node(75, "Test Movie 2")
        expected = [{"Test Movie": 50}, {"Test Movie 2": 75}]

        self.assertEqual(tree.sort(), expected)

    def test_tree_sorts_both(self):
        tree = bs.BinarySearchTree()
        tree.insert_node(50, "Test Movie")
        tree.insert_node(75, "Test Movie 2")
        tree.insert_node(25, "Test Movie 3")
        expected = [{"Test Movie 3": 25}, {"Test Movie": 50}, {"Test Movie 2": 75}]

        self.assertEqual(tree.sort(), expected)

    def test_tree_sorts_multiple(self):
        tree = bs.BinarySearchTree()
        tree.insert_node(50, "Test Movie")
        tree.insert_node(45, "Test Movie 2")
        tree.insert_node(55, "Test Movie 3")
        tree.insert_node(60, "Test Movie 4")
        tree.insert_node(11, "Test Movie 5")
        tree.insert_node(85, "Test Movie 6")
        tree.insert_node(53, "Test Movie 7")
        expected = [{"Test Movie 5": 11}, {"Test Movie 2": 45}, {"Test Movie": 50}, {"Test Movie 7": 53}, {"Test Movie 3": 55}, {"Test Movie 4": 60}, {"Test Movie 6": 85}]

        self.assertEqual(tree.sort(), expected)

    def test_tree_loads_file(self):
        tree = bs.BinarySearchTree()
        tree.load("test/movies.txt")
        tree.sort

        self.assertEqual(len(tree.sort()), 6)

    def test_tree_shows_health(self):
        tree = bs.BinarySearchTree()
        tree.insert_node(50, "Test Movie")

        self.assertEqual(tree.get_health(0), [[50, 1, 100]])

    def test_tree_shows_health_multiple(self):
        tree = bs.BinarySearchTree()
        tree.insert_node(50, "Test Movie")
        tree.insert_node(45, "Test Movie 2")
        tree.insert_node(55, "Test Movie 3")
        tree.insert_node(60, "Test Movie 4")
        tree.insert_node(11, "Test Movie 5")
        tree.insert_node(85, "Test Movie 6")
        tree.insert_node(53, "Test Movie 7")
        tree.insert_node(12, "Test Movie 8")
        tree.insert_node(54, "Test Movie 9")
        tree.insert_node(59, "Test Movie 10")
        tree.insert_node(47, "Test Movie 11")
        tree.insert_node(46, "Test Movie 12")


        self.assertEqual(tree.get_health(0), [[50,12,100]])
        self.assertEqual(tree.get_health(1), [[45, 5, 41], [55, 6, 50]])
        self.assertEqual(tree.get_health(2), [[11, 2, 16], [47, 2, 16], [53, 2, 16], [60, 3, 25]])
        self.assertEqual(tree.get_health(3), [[12, 1, 8], [46, 1, 8], [54, 1, 8], [59, 1, 8], [85, 1, 8]])
        self.assertEqual(tree.get_health(4), [])

if __name__ == '__main__':
    unittest.main()
