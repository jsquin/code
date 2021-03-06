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
    # you are passed in a list of >50,000 English words.
    # Return a subset of that list containing all the words that are length 5.
    # Also filter out words with special characters.
    "* YOUR CODE HERE *"

# ----------------------------------- END PART 1 ----------------------------------- #


def generate_new_wordlist(long = False):
    if long:
        file = "words.txt"
    else:
        file = "wordsshort.txt"
    with open(file) as f:
        new_list = []
        for line in f:
            if "-" not in line and "'" not in line and "#" not in line:
                new_list.append(line[:-1].lower())
    return new_list 

def generate_final_wordlist(long = False):
    if long:
        file = "wordsfinal.txt"
    else:
        file = "wordsshortfinal.txt"
    with open(file, "w+") as f:
        words = only_length_5(generate_new_wordlist())
        for word in words:
            f.write(word + "\n")

def read_wordlist(long = False):
    if long:
        file = "wordsfinal.txt"
    else:
        file = "wordsshortfinal.txt"
    with open(file, "r") as f:
        words = [] 
        for line in f:
            words.append(line[:-1])
    return words 

class Wordle:
    def __init__(self, babymode = True, letter_help = True, long = False):
        self.done = False
        self.guess_strings, self.guess_results = [], []
        self.wordlist = read_wordlist(long)
        self.word = random.choice(self.wordlist) 
        self.record = dict()
        for i in range(7):
            self.record[i] = 0 
        self.babymode, self.letter_help = babymode, letter_help
        
# ---------------------------------- START PART 2 ---------------------------------- #
    def compare(self, input):
        # Takes in a string of length 5 and returns the Wordle status
        # Wordle status should be formatted as a list of length 5, containing
        # 0 for Incorrect, 1 for wrong position, and 2 for correct

        # This part is open ended. A guideline is provided but you may
        # choose to ignore it.

        return # To suppress errors. Remove this line
        "* YOUR CODE HERE *"
        response = ______
        for i in ______ :
            if input[i] == ______:
                response[i] = ______
            else:
                for j in ______:
                    if input[i] == ______ and input[j] != ______: 
                        response[i] = ______
                        break 
        return response
# ----------------------------------- END PART 2 ----------------------------------- #
    
    def run_game(self):
        # You don't need to worry about this function
        os.system('clear')
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
        # You don't need to worry about this function
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

    def reset(self):
        # You don't need to worry about this function
        usr_inp = input("Would you like to play again? (yes or no)\n")
        while True:
            if usr_inp.lower() in ["y", "ye", "yes"]:
                self.guess_strings, self.guess_results = [], []
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
        self.guess_strings, self.guess_results = guess_strings, guess_results
        self.solveriters = solveriters
        self.opener = opener
        self.done = False
        self.wordlist = read_wordlist(long)

# ---------------------------------- START PART 3 ---------------------------------- #
    def filter(self, result, string, wordlist):
        # Filters the wordlist based on a given guess string and its result
        # This part is open ended. A guideline is provided, but you may choose 
        # to ignore it.

        return # To suppress errors. Remove this line
        "* YOUR CODE HERE *"
        letters_correct = []
        for i in ______:
            if result[i] == 2:
                letters_correct.append(______)
        def filter_word(word):
            for i in ______:
                if result[i] == ______ and not word.______ <= letters_correct.______:
                    return False 
                elif result[i] == ______ and not ______:
                    return False 
                elif result[i] == ______ and not ______:
                    return False 
            return True 
        filtered_words = []
        for word in ______:
            if filter_word(______):
                filtered_words.append(______)
        return filtered_words
# ----------------------------------- END PART 3 ----------------------------------- #

    def run_solver(self, verbose = True):
        # You don't need to worry about this function
        wordle = Wordle()
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
        return sum([i * wordle.record[i] for i in range(1,7)]) / self.solveriters

    def manual_solver(self):
        # You don't need to worry about this function
        temp_wordlist = self.wordlist
        wordle = Wordle()
        os.system("clear")
        wordle.print_state()
        while not self.done:
            usr_inp = input("Please input your word choice\n")
            if usr_inp in ["q", "quit", "e", "exit"]:
                os.system("clear")
                self.done = True 
                break 
            if len(usr_inp) != 5:
                print("Word choice must have 5 letters")
            elif usr_inp.lower() not in self.wordlist:
                print("Not a valid word")
            else:
                word = usr_inp 
                sanitized = False
                while not sanitized:
                    flag = False 
                    usr_inp = input("Please input the result as comma-separated integers. (e.g.: '0,2,1,0,0)\n") + ","
                    for i in range(5):
                        if usr_inp[i*2] not in ["0","1","2"] or usr_inp[i*2+1] != ",":
                            flag = True 
                            print("Malformed input!")
                            break 
                    if not flag:
                        sanitized = True
                        final_val = []
                        for j in range(5):
                            final_val.append(int(usr_inp[j*2]))
                wordle.guess_strings.append(word)
                wordle.guess_results.append(final_val)
                temp_wordlist = self.filter(final_val, word, temp_wordlist)
                wordle.print_state()
                if final_val == [2,2,2,2,2] or len(wordle.guess_strings) == 6:
                    if final_val == [2,2,2,2,2]:
                        print("Congrats! You found '" + word + "' in " + str(len(wordle.guess_strings)) + " tries.")
                    else:
                        print("Nice try.")
                    flag2 = False
                    while not flag2:
                        usr_inp = input("Would you like to continue?\n")
                        if usr_inp.lower() in ["no", "n"]:
                            self.done = True
                            flag2 = True 
                            break 
                        elif usr_inp.lower() not in ["yes", "y"]:
                            print("Please answer yes or no")
                        else:
                            flag2 = True
                            wordle = Wordle()
                            os.system("clear")
                            temp_wordlist = self.wordlist
                            wordle.print_state()
                else:
                    print("Possible Words: \n")
                    print(temp_wordlist)