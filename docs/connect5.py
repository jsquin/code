import os 
import random

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMS = "0123456789"

class AI:
    def __init__(self):
        self.mode = 1 # Heuristic

    def make_move(self, grid, player):
        val = -1 
        if player:
            val = 1 
        if self.mode == 0: # Random Mode
            possible_moves = []
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    if grid[i][j] == 0:
                        possible_moves.append((i, j))
            loc = random.choice(possible_moves)
            return loc, val 
        elif self.mode == 1: # Simple Heuristic Mode: Center Seeking
            center = [len(grid) // 2, len(grid[0]) // 2]
            closest = (0,0, (center[0] ** 2 + center[1] ** 2) ** 0.5)
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    if grid[i][j] == 0:
                        if ((center[0] - i) ** 2 + (center[1] - j) ** 2) ** 0.5 < closest[2]:
                            closest = (i, j, ((center[0] - i) ** 2 + (center[1] - j) ** 2) ** 0.5)
            return (closest[0], closest[1]), val 

        elif self.mode == 2: # Exhaustive Search Mode
            return loc, val 

        elif self.mode == 3: # Short Search Mode 
            return loc, val 
        else:
            print("NOT IMPLEMENTED")


    def score(self, grid):
        # Return the score of a grid 
        # Heuristic 1:
        return

class ConnectN:
    def __init__(self, N = 5, gridsize = (9,9), AI_P1 = False, AI_P2 = False):
        self.N = N
        self.gridsize = gridsize
        self.grid = self.generate_grid(self.gridsize[0], self.gridsize[1])
        self.AI_P1, self.AI_P2 = AI_P1, AI_P2
        self.done = False
        self.turn = True
        self.AI = AI()

    def generate_grid(self, height, width):
        grid = []
        for i in range(height):
            row = []
            for j in range(width):
                row.append(0)
            grid.append(row)
        return grid 

    def draw_grid(self):
        os.system("clear")
        string = "     " 
        for i in range(len(self.grid)):
            string += "  " + ALPHABET[i] + " "
        print(string)
        for i in range(len(self.grid)):
            print("     " + "----" * len(self.grid) + "-")
            if i < 10:
                gap = "   "
            elif i < 100:
                gap = "  "
            string = str(i) + "." + gap + "| "
            for j in range(len(self.grid[i])):
                if self.grid[i][j] == 0:
                    string += " "
                elif self.grid[i][j] == 1:
                    string += '\033[92mX\033[0m'
                else:
                    string += '\033[91mO\033[0m' 
                string += " | "
            print(string)
        print("     " + "----" * len(self.grid) + "-")

    def check_win(self, location, val):
        # Is called every time a tile is placed. Returns true if winning tile
        # Check horizontal
        run, temp = 1, location[1]
        while temp > 0:
            temp -= 1
            if self.grid[location[0]][temp] == val:
                run += 1
            else:
                break 
        temp = location[1]
        while temp < self.gridsize[1]-1:
            temp += 1
            if self.grid[location[0]][temp] == val: 
                run += 1 
            else:
                break 
        if run >= self.N:
            return True

        # Check Vertical
        run, temp = 1, location[0]
        while temp > 0:
            temp -= 1
            if self.grid[temp][location[1]] == val:
                run += 1
            else:
                break 
        temp = location[0]
        while temp < self.gridsize[0] - 1:
            temp += 1
            if self.grid[temp][location[1]] == val: 
                run += 1 
            else:
                break 
        if run >= self.N:
            return True

        # Check positive diagonal 
        run, temp1, temp2 = 1, location[0], location[1]
        while temp1 > 0 and temp2 > 0:
            temp1 -= 1
            temp2 -= 1 
            if self.grid[temp1][temp2] == val:
                run += 1
            else:
                break 
        temp1, temp2 = location[0], location[1]
        while temp1 < self.gridsize[0] - 1 and temp2 < self.gridsize[1] - 1:
            temp1 += 1
            temp2 += 1 
            if self.grid[temp1][temp2] == val: 
                run += 1 
            else:
                break 
        if run >= self.N:
            return True

        # Check negative diagonal 
        run, temp1, temp2 = 1, location[0], location[1]
        while temp1 < self.gridsize[0] - 1 and temp2 > 0:
            temp1 += 1
            temp2 -= 1 
            if self.grid[temp1][temp2] == val:
                run += 1
            else:
                break 
        temp1, temp2 = location[0], location[1]
        while temp1 > 0 and temp2 < self.gridsize[1] - 1:
            temp1 -= 1
            temp2 += 1 
            if self.grid[temp1][temp2] == val: 
                run += 1 
            else:
                break 
        if run >= self.N:
            return True
        return False

    def make_move(self, player):
        if player:
            text, val = "Player 1", 1
        else:
            text, val = "Player 2", -1
        flag2 = False 
        while not flag2:
            flag = False
            while not flag:
                fail = False
                usr_inp = input("Where would " + text + " like to place a tile? \n(e.g.: 'B3', 'G10')\n")
                if usr_inp.lower() in ["q", "quit", "e", "exit"]:
                    self.done = True 
                    self.gameover = True 
                    return 
                if usr_inp[0].lower() in ALPHABET.lower():
                    index1 = ALPHABET.lower().find(usr_inp[0].lower())
                    for char in usr_inp[1:]:
                        if char not in NUMS:
                            fail = True 
                else:
                    fail = True
                if fail:
                    self.draw_grid()
                    print("Please input a Letter and Number (e.g.: 'B3', 'G10')")
                else:
                    index2 = int(usr_inp[1:])
                    flag = True 
            if not (self.gridsize[0] > index2 and self.gridsize[1] > index1) or self.grid[index2][index1] != 0:
                self.draw_grid()
                print(usr_inp + " is not a valid location!")
            else:
                self.grid[index2][index1] = val 
                flag2 = True 
        if self.check_win((index2, index1), val):
            if player:
                text = '\033[92m' + text + '\033[0m'
            else:
                text = '\033[91m' + text + '\033[0m'
            self.end_game(text)
        
    def reset(self):
        self.grid = self.generate_grid(self.gridsize[0], self.gridsize[1])
        self.turn = False 

    def end_game(self, winner):
        os.system("clear")
        self.draw_grid()
        flag = False 
        usr_inp = input(winner + " wins!\nWould you like to play again? (yes or no)\n")
        while not flag:
            if usr_inp.lower() in ["y","ye","yes"]:
                self.reset()
                flag = True
            elif usr_inp.lower() in ["n", "no"]:
                self.done = True 
                return 
            else:
                usr_inp = input("Please answer yes or no\n")

    def run_game(self):
        while not self.done:
            self.draw_grid()
            if self.turn and self.AI_P1 or (not self.turn and self.AI_P2):
                loc, val = self.AI.make_move(self.grid, self.turn)
                self.grid[loc[0]][loc[1]] = val
                if self.check_win(loc, val):
                    if self.turn:
                        text = '\033[92m' + "Player 1" + '\033[0m'
                    else:
                        text = '\033[91m' + "Player 2" + '\033[0m'
                    self.end_game(text)
            else:
                self.make_move(self.turn)
            self.turn = not self.turn
        os.system("clear")
        
game = ConnectN()
game.AI_P2 = True
game.run_game()