# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import unittest
import sys
sys.path.append('/Users/danielshin/Documents/turing/other/python/date_night_python/lib')

import node as n

class NodeTest(unittest.TestCase):

    def test_node_can_hold_data(self):
        node =  n.Node(100, "Test Movie")
        expected = {"Test Movie": 100}

        self.assertEqual(node.data, expected)

    def test_node_starts_with_no_link(self):
        node =  n.Node(100, "Test Movie")
        self.assertEqual(node.left, None)

if __name__ == '__main__':
    unittest.main()
