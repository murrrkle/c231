# CPSC 231 Assignment 5: Reversi                                                                                          ID 10099049; Michael Hung

###################################################################################################################################################

import random

class Game:
	delta = [[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1]]

	turns = 4

	def __init__(self, board, turn):
		self.board = board
		self.turn = turn
		self.moves = self.get_moves()

        # check_move evaluates the validity of a move chosen in get_moves
	def check_move(self, move, d):
            
                flag = False
                i, j = move[0], move[1]
                cnt = 0
                
                while flag == False:
                    i, j = i + self.delta[d][0], j + self.delta[d][1] # Moves the checking space to one square in direction d
                    if i < 0 or i > 7 or j < 0 or j > 7: return False # i.e. Invalid move if space is outside of the board
                    if self.board[i][j] == -1: return False # i.e. Invalid move if the space is empty
                    elif self.board[i][j] == self.turn and cnt > 0: flag = True # The player's piece has been found and an opponent's piece has been found prior. Valid move. Break out of loop.
                    elif self.board[i][j] == self.turn: return False # The player's piece has been found, but an opponent's piece has not yet been found. Invalid move.
                    elif self.board[i][j] == 1 - self.turn: cnt += 1 # An opponent's piece has been found. Re-iterate.

                return (flag and cnt > 0) # Returns True - i.e. Valid move

        # get_moves appends all possible moves for a given turn into a list self.moves
	def get_moves(self):

                self.moves = [] # This list will hold all valid moves for the turn. Reset at the beginning of each turn.

                for i in range(8):
                    for j in range(8): # Checks all board spaces
                        if self.board[i][j] == -1: # Only checks spaces that are empty
                            for d in range(8): # Checks all directions
                                if self.check_move([i, j], d): self.moves += [[i, j]] # Appends valid moves to list self.moves

        # select_move determines the strategy for the AI opponent
	def select_move(self):
                  
                    flag = False
                    for i in range(8):
                        for j in range(8):
                            for move in [[i, 0], [0, j], [i, 7], [7, j]]: # Checks all edge squares including corners
                                if move in self.moves:
                                    if move in [[0,0], [0, 7], [7, 0], [7, 7]]: # Checks for corners. If corner is valid, corner is top priority.
                                        Game.turns += 1
                                        return move

                                    if move in [[0, 1], [1, 0], [1, 1], [7, 1], [6, 0], [6, 1], [0, 6], [1, 7], [1, 6], [6, 6], [7, 6], [6, 7]]: # Checks if space is adjacent to corner.
                                        if len(self.moves) > 1:
                                            Game.turns += 1
                                            return self.moves[1] # If the space is available and it is not the only one, return the second move in the list self.moves. Hopefully it isn't an adjacent one.
                                        else:
                                            Game.turns += 1 # If the adjacent space is the only available space, take it.
                                            return move
                                else:
                                    Game.turns += 1
                                    return self.moves[0] #If the edge space is unavailable, take the first move in list self.moves.


	def play_move(self, move): 
		m, n = move[0], move[1]
		for d in range(8):
			i, j = m, n
			if self.check_move(move, d):
				i, j = i+self.delta[d][0], j+self.delta[d][1]
				while self.board[i][j] == 1-self.turn:
					self.board[i][j] = self.turn
					i, j = i+self.delta[d][0], j+self.delta[d][1]
		self.board[m][n]=self.turn

	def final_result(self): 
		black, white = 0, 0   # color 0 is white
		for i in range(8):
			for j in range(8):
				if self.board[i][j] == 0: white += 1
				elif self.board[i][j] == 1: black += 1
		return white,black


		

