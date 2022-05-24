###########################
#                         #
#    Project 1: Wordle    #
#  Written by Marcus Lee  #
#                         #
###########################

from Wordle import *

MODE = 1

if MODE == 0:
    game = Wordle()
    game.run_game()
elif MODE == 1:
    solver = WordleSolver()
    solver.opener = "raise"
    solver.run_solver()
elif MODE == 2:
    test_words = ["raise", "crane"]
    solver = WordleSolver()
    # TODO: Implement Best opener checker

