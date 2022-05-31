###########################
#                         #
#    Project 1: Wordle    #
#  Written by Marcus Lee  #
#                         #
###########################

import os
import sys
from Wordle import *

def add_to_file(filename, line):
    with open(filename, "a") as f:
        f.write(line + "\n")

if __name__ == "__main__":
    MODE = 0 
    if len(sys.argv) > 1:
        if len(sys.argv[1]) == 1 and sys.argv[1][0] in "01234":
            MODE = int(sys.argv[1][0])
        else:
            MODE = None
            print("Malformed argument")
    if MODE == 0: #Wordle Game
        game = Wordle()
        game.run_game()
    elif MODE == 1: # Statistics for one opener
        sanitized = False
        solver = WordleSolver()
        solver.solveriters = 10000
        while not sanitized:
            usr_inp = input("Please input a word\n")
            if usr_inp not in solver.wordlist:
                print("Invalid word")
            else:
                solver.opener = usr_inp 
                sanitized = True 
        print(solver.run_solver())
    elif MODE == 2: # Best opener
        test_words = read_wordlist()
        solver = WordleSolver()
        solver.solveriters = 5000
        for word in test_words:
            solver.opener = word 
            add_to_file("record.txt", word + " " + str(solver.run_solver(verbose = False))) 
            os.system("clear")
            print("Calculating Best Wordle Opener.")
            print(word)
    elif MODE == 3: #Record Reader
        biggest = (None, 0)
        smallest = (None, float('inf'))
        with open("record.txt", "r") as f:
            for line in f:
                word, val = line[:line.find(" ")], float(line[line.find(" ") + 1:-1])
                if biggest[1] < val:
                    biggest = (word, val)
                if smallest[1] > val:
                    smallest = (word, val)
        print(biggest, smallest)
    elif MODE == 4: #Wordle Solver
        solver = WordleSolver() 
        solver.manual_solver()




