###########################
#                         #
#    Project 1: Wordle    #
#  Written by Marcus Lee  #
#                         #
###########################

# Part 1:
#   Generate word bank

# Part 2:
#   Create Wordle Class

# Part 3:
#   Wordle Class Methods
#   Maybe implement a wordle helper?
#   It deletes letters and stuff?
#   Maybe implement a wordle solver / helper
#   Generate a list of possible words given the information.


#New plan: Wordle Game and Wordle Solver

# Part 4:
#   Keep record of score 



# Part 1

def only_length_5(wordlist): 
    # you are passed in a list of 58000 English words.
    # Return a subset of that list containing all the words that are length 5.
    "* YOUR CODE HERE *"

    new_words = [] 
    for word in wordlist:
        if len(word) == 5:
            new_words.append(word)
    return new_words 

def generate_new_wordlist():
    with open("words.txt") as f:
        new_list = []
        for line in f:
            new_list.append(line[:-1])
    return new_list 

def generate_final_wordlist():
    with open("finalwords.txt", "w+") as f:
        words = only_length_5(generate_new_wordlist())
        for word in words:
            f.write(word + "\n")

def read_wordlist():
    with open("finalwords.txt", "r") as f:
        words = [] 
        for line in f:
            words.append(line[:-1])
    return words 


class Wordle:
    def __init__(self, word):
        self.word = word 
        self.guesses = 0
        self.guess_strings = []

    def compare(self, input):
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
    
    def run_game(self):
        # TODO
        return

    
class WordleGame:
    def __init__(self):
        self.game = None
        self.word = None 
        self.record = []

    def run_game(self):
        return
