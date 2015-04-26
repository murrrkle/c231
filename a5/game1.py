# CPSC 231 Assignment 5: Reversi                                  ID 10099049; Michael Hung

###########################################################################################


import random

class Game:
	delta = [[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1]]

	turns = 4

	def __init__(self, board, turn):
		self.board = board
		self.turn = turn
		self.moves = self.get_moves()

	def check_move(self, move, d):
            
                flag = False
                i, j = move[0], move[1]
                cnt = 0
                
                while flag == False:
                    i, j = i + self.delta[d][0], j + self.delta[d][1]
                    if i < 0 or i > 7 or j < 0 or j > 7: return False
                    if self.board[i][j] == -1: return False
                    elif self.board[i][j] == self.turn and cnt > 0: flag = True
                    elif self.board[i][j] == self.turn: return False
                    elif self.board[i][j] == 1 - self.turn: cnt += 1

                return (flag and cnt > 0)

	def get_moves(self):

                self.moves = []

                for i in range(8):
                    for j in range(8):
                        if self.board[i][j] == -1:
                            for d in range(8):
                                if self.check_move([i, j], d): self.moves += [[i, j]]


	def select_move(self):
                  
                    flag = False
                    for i in range(8):
                        for j in range(8):
                            for move in [[i, 0], [0, j], [i, 7], [7, j]]:
                                if move in self.moves:
                                    

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


		

