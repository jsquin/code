###########################
#                         #
#   Project 1 Autograder  #
#  Written by: Marcus Lee #
#                         #
###########################

import unittest
from Wordle import * 

# Part 1

# Check 'wordsshortfinal.txt' and 'finalwords'

# Check that the files have the right length 

# Check that the function works on manual examples

class Q1_Manual(unittest.TestCase):
    # Testing only_length_5(wordlist)
    def test1(self):
        # Empty List
        self.assertEqual(only_length_5([]), [], "Should be an empty list")
    def test2(self):
        # Non-alphabetical characters
        self.assertEqual(only_length_5(["1","22","333","4444","55555","666666","onlyy","length","five!"]),["onlyy"], "Should be ['onlyy']")
    def test3(self):
        # Special characters
        self.assertEqual(only_length_5([]), [], "Should be False")
    def test4(self):
        temp = ["this", "is", "a", "test", ",", "to", "see", "if th", "ethin", "works", "prope", "rly"]
        self.assertEqual(only_length_5(temp), ["ethin", "prope"], "Should be length 2")


# Part 2

# Manual Testing Different words
class Q2(unittest.TestCase):
    # Testing Wordle.compare
    def test1(self):
        wordle = Wordle()
        wordle.word = "raise"
        self.assertEqual(wordle.compare("raise"), [2,2,2,2,2])
    def test2(self):
        wordle = Wordle()
        wordle.word = "raise"
        self.assertEqual(wordle.compare("saire"), [1,2,2,1,2])
    def test3(self):
        wordle = Wordle()
        wordle.word = "raise"
        self.assertEqual(wordle.compare("zzzzz"), [0,0,0,0,0])
    def test4(self):
        wordle = Wordle()
        wordle.word = "raise"
        self.assertEqual(wordle.compare("rzzez"), [2,0,0,1,0])

# More Testing


# Part 3

# Manual Wordlist Shortening
class Q3(unittest.TestCase):
    # Testing WordleSolver.filter(result, string, wordlist)
    # Assumes wordle is complete.
    def test1(self):
        solver = WordleSolver()
        wordle = Wordle()
        wordle.word = "raise"
        result = wordle.compare("hello")
        self.assertEqual(wordle.compare("raise"), [2,2,2,2,2])
    def test2(self):
        solver = WordleSolver()
        wordle.word = "raise"
        self.assertEqual(wordle.compare("saire"), [1,2,2,1,2])
    def test3(self):
        solver = WordleSolver()
        wordle.word = "raise"
        self.assertEqual(wordle.compare("zzzzz"), [0,0,0,0,0])
    def test4(self):
        solver = WordleSolver()
        wordle.word = "raise"
        self.assertEqual(wordle.compare("rzzez"), [2,0,0,1,0])


if __name__ == '__main__':
    unittest.main()