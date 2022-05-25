###########################
#                         #
#    Project 1: Wordle    #
#  Written by Marcus Lee  #
#                         #
###########################

import os 
import random

# Part 1: Generate word bank
# Part 2: Wordle Game
# Part 3: Wordle Solver
# Part 4: For fun: Find the best wordle opener


# ---------------------------------- START PART 1 ---------------------------------- #
def only_length_5(wordlist): 
    # PART 1: GENERATE WORD BANK
    # you are passed in a list of 58000 English words.
    # Return a subset of that list containing all the words that are length 5.
    "* YOUR CODE HERE *"
    new_words = [] 
    for word in wordlist:
        if len(word) == 5:
            new_words.append(word)
    return new_words 
# ----------------------------------- END PART 1 ----------------------------------- #

def generate_new_wordlist():
    with open("wordsmany.txt") as f:
        new_list = []
        for line in f:
            if "-" not in line and "'" not in line and "#" not in line:
                new_list.append(line[:-1].lower())
    return new_list 

def generate_final_wordlist():
    with open("finalwordsmany.txt", "w+") as f:
        words = only_length_5(generate_new_wordlist())
        for word in words:
            f.write(word + "\n")

def read_wordlist(long = False):
    if long:
        file = "finalwords.txt"
    else:
        file = "finalwordsmany.txt"
    with open(file, "r") as f:
        words = [] 
        for line in f:
            words.append(line[:-1])
    return words 

class Wordle:
    def __init__(self, babymode = False, letter_help = True, long = False):
        self.done = False
        self.guess_strings = []
        self.guess_results = []
        self.wordlist = read_wordlist(long)
        self.word = random.choice(self.wordlist) 
        self.record = dict()
        for i in range(7):
            self.record[i] = 0 
        self.babymode, self.letter_help = babymode, letter_help
        
# ---------------------------------- START PART 2 ---------------------------------- #
    def compare(self, input):
        # PART 2: WORDLE GAME
        # Takes in a string of length 5 and returns the Wordle status
        # Wordle status should be formatted as a list of length 5, containing
        # 0 for Incorrect, 1 for wrong position, and 2 for correct
        response = [0] * 5 
        for i in range(5):
            if input[i] == self.word[i]: # Check if letter is correct
                response[i] = 2 
            else:
                for j in range(5):
                    if input[i] == self.word[j] and input[j] != self.word[j]: # Check if letter is in string and hasn't been marked correct.
                        response[i] = 1
                        break 
        return response
# ----------------------------------- END PART 2 ----------------------------------- #
    
    def run_game(self):
        os.system('clear')
        usr_inp = ""
        self.print_state()
        while not self.done:
            usr_inp = input("Guess a word\n").lower()
            if usr_inp.lower() in ["q", "quit", "e", "exit"]:
                return 
            if self.word == None:
                self.word = random.choice(self.wordlist)
            if usr_inp.lower() in ["give up", "ff"]:
                self.reset()
            elif len(usr_inp) != 5:
                print("User input must a word of length 5!")
            elif self.babymode and usr_inp not in self.wordlist: # Baby mode forces user inputs to be known words
                print("Not a valid word!") 
            else:
                self.guess_strings.append(usr_inp)
                self.guess_results.append(self.compare(usr_inp))
                self.print_state()
                if self.guess_results[-1] == [2,2,2,2,2]:
                    tries = lambda guesses: " try" if guesses == 1 else " tries"
                    print("Congrats! You beat the Wordle in " + str(len(self.guess_strings)) + tries(len(self.guess_strings)))
                    self.reset()
                    self.record[len(self.guess_strings)] += 1
                elif len(self.guess_strings) == 6:
                    print("Nice try! The word was '" + self.word + "'")
                    self.record[0] += 1
                    self.reset()

    def print_state(self):
        alphabet, banned, unbanned = "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "", ""
        os.system('clear')
        print("------- WORDLE ------")
        for i in range(len(self.guess_strings)):
            output_word = "| "
            for j in range(5):
                if self.guess_results[i][j] == 0:
                    banned += self.guess_strings[i][j].upper()
                    output_word += '\033[90m' + self.guess_strings[i][j].upper() + '\033[0m' + " | "
                elif self.guess_results[i][j] == 1:
                    output_word += '\033[93m' + self.guess_strings[i][j].upper() + '\033[0m' + " | "
                elif self.guess_results[i][j] == 2:
                    unbanned += self.guess_strings[i][j].upper()
                    output_word += '\033[92m' + self.guess_strings[i][j].upper() + '\033[0m' + " | "
            print(output_word)
        for i in range(6 - len(self.guess_strings)):
            output_word = "| "
            for j in range(5):
                output_word += '\033[90m' + "_" + '\033[0m' + " | "
            print(output_word)
        if self.letter_help:
            output_word = "\n"
            for letter in alphabet:
                if letter in banned and letter not in unbanned:
                    output_word += '\033[90m' + letter + '\033[0m' + " "
                else:
                    output_word += letter + " "
                if letter == "K" or letter == "V":
                    output_word += "\n"
            print(output_word + "\n")

    def reset(self): # TODO: Need to update record
        usr_inp = input("Would you like to play again? (yes or no)\n")
        while True:
            if usr_inp.lower() in ["y", "ye", "yes"]:
                self.guess_strings = []
                self.guess_results = []
                self.word = None 
                os.system('clear')
                self.print_state()
                return
            elif usr_inp.lower() in ["n", "no"]:
                self.done = True 
                os.system('clear')
                return
            else:
                usr_inp = input("Please answer yes or no\n")

class WordleSolver:
    def __init__(self, guess_strings = [], guess_results = [], opener = None, solveriters = 100, long = False):
        self.guess_strings = guess_strings 
        self.guess_results = guess_results 
        self.solveriters = solveriters
        self.opener = opener
        self.long = long

# ---------------------------------- START PART 3 ---------------------------------- #
    def filter(self, result, string, wordlist):
        # PART 3: WORDLE SOLVER
        # Filters the wordlist based on a given guess string and its result
        letters_in = []
        for i in range(5):
            if result[i] == 2:
                letters_in.append(string[i])
            else:
                letters_in.append("")
        def filter_word(word):
            for i in range(5):
                if result[i] == 0 and not word.count(string[i]) <= letters_in.count(string[i]):
                    return False 
                elif result[i] == 1 and not (string[i] in word and word[i] != string[i]):
                    return False 
                elif result[i] == 2 and not (string[i] == word[i]):
                    return False 
            return True 
        filtered_words = []
        for word in wordlist:
            if filter_word(word):
                filtered_words.append(word)
        return filtered_words
# ----------------------------------- END PART 3 ----------------------------------- #

    def filter_all(self):
        words = read_wordlist()
        for i in range(len(self.guess_strings)):
            words = self.filter(self.guess_results[i], self.guess_strings[i], words)
        return words 

    def run_solver(self, verbose = True):
        wordle = Wordle(long = self.long)
        for _ in range(self.solveriters):
            wordlist = wordle.wordlist
            for i in range(6):
                if i == 0 and self.opener != None:
                    guess = self.opener 
                else:
                    guess = random.choice(wordlist)
                wordle.guess_strings.append(guess)
                wordle.guess_results.append(wordle.compare(guess))
                if verbose:
                    wordle.print_state()
                wordlist = self.filter(wordle.guess_results[i], wordle.guess_strings[i], wordlist)
                if wordle.guess_results[i] == [2, 2, 2, 2, 2]:
                    wordle.record[i+1] += 1 
                    break 
                if i == 6:
                    wordle.record[0] += 1
            wordle.guess_strings = []
            wordle.guess_results = []
            wordle.word = random.choice(wordle.wordlist) 
        # for i in range(7):
        #     print(str(i) + ": " + str(wordle.record[i]))
        # print("avg: " + str((wordle.record[1] + wordle.record[2]*2+wordle.record[3]*3+wordle.record[4]*4+wordle.record[5]*5+wordle.record[6]*6)/self.solveriters))
        return (wordle.record[1] + wordle.record[2]*2+wordle.record[3]*3+wordle.record[4]*4+wordle.record[5]*5+wordle.record[6]*6)/self.solveriters

    def manual_solver(self):
        # To be run alongside wordle. A cheat engine.
        return