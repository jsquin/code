###########################
#                         #
#    Project 1: Wordle    #
#  Written by Marcus Lee  #
#                         #
###########################

import os
from Wordle import *

MODE = 2

def add_to_file(filename, line):
    with open(filename, "a") as f:
        f.write(line + "\n")

if MODE == 0: #Wordle Game
    game = Wordle()
    game.run_game()
elif MODE == 1: # Statistics for one opener
    solver = WordleSolver(long = True)
    solver.solveriters = 2000
    solver.opener = "aeors"
    print(solver.run_solver())
elif MODE == 2: # Best opener
    test_words = read_wordlist(long = True)
    solver = WordleSolver(long = True)
    solver.solveriters = 2000
    for word in test_words:
        solver.opener = word 
        add_to_file("record.txt", word + " " + str(solver.run_solver(verbose = False))) 
        os.system("clear")
        print(word)



