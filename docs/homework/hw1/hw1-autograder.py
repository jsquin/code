###########################
#                         #
#  Homework 1 Autograder: #
#  Written by Marcus Lee  #
#   Course Content from   #
#    Berkeley's CS61A     #
#                         #
###########################

import unittest
from hw1 import * 

class Q1(unittest.TestCase):
    # Testing k_in_num(k, num)
    def test1(self):
        self.assertEqual(k_in_num(3, 123), True, "Should be True")
    def test2(self):
        self.assertEqual(k_in_num(2, 123), True, "Should be True")
    def test3(self):
        self.assertEqual(k_in_num(5, 123), False, "Should be False")
    def test4(self):
        self.assertEqual(k_in_num(0, 0), False, "Should be False")

class Q2(unittest.TestCase):
    # Testing a_plus_abs_b(a, b)
    def test1(self):
        self.assertEqual(a_plus_abs_b(2, 3), 5, "Should be 5")
    def test2(self):
        self.assertEqual(a_plus_abs_b(2, -3), 5, "Should be 5")
    def test3(self):
        self.assertEqual(a_plus_abs_b(-1, 4), 3, "Should be 3")
    def test4(self):
        self.assertEqual(a_plus_abs_b(-1, -4), 3, "Should be 3")

class Q3(unittest.TestCase):
    # Testing two_of_three(i, j, k)
    def test1(self):
        self.assertEqual(two_of_three(1, 2, 3), 5, "Should be 5")
    def test2(self):
        self.assertEqual(two_of_three(5, 3, 1), 10, "Should be 10")
    def test3(self):
        self.assertEqual(two_of_three(10, 2, 8), 68, "Should be 68")
    def test4(self):
        self.assertEqual(two_of_three(5, 5, 5), 50, "Should be 50")

class Q4(unittest.TestCase):
    # Testing largest_factor(n)
    def test1(self):
        self.assertEqual(largest_factor(15), 5, "Should be 5")
    def test2(self):
        self.assertEqual(largest_factor(80), 40, "Should be 40")
    def test3(self):
        self.assertEqual(largest_factor(13), 1, "Should be 1")

if __name__ == '__main__':
    unittest.main()
