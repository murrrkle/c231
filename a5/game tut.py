import random

class Game:
	delta = [[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1]]

	def __init__(self, board, turn):
		self.board = board
		self.turn = turn
		self.moves = self.get_moves()

	def check_move(self, move, d):
                
		i, j = move[0], move[1]
		# loop: increase i, j by self.delta[d][] each time and test for validity each iteration
                # cnt = 0 OR flag = False
		# either use a counter to count the pieces or use a boolean flag
		# if self.board[i][j] == self.turn, then STOP and check if cnt > 0 or the flag is True. If not, it isn't a valid move.
		# if self.board[i][j] == 1 - self.turn: cnt += 1 OR flag = True
		# If self.board[i][j] == -1, then there is no space there. flag = False
		# return flag == True and cnt > 0
		

	def get_moves(self):
                mo = []
		# Go through all the places in the self.board (two loops)
		# when is board[i][j] valid? When the space is -1 and when self.check_move([i, j], d) == True for d in each direction (use another loop)
		# If board[i][j] is valid, append it to mo
		

	def select_move(self):
		# If you are lazy, just select a move at random.
		# random number r = random.randint(0, -1)
		# return your move

		#IF YOU WANT AN A+

		# in select_move()...

		#The strategy is:
		# 1) GET THE CORNERS AND THE EDGES. Corners are the first priority. Use an iteration and if statement to check if the corner is a valid move.
		# 2) DO NOT get the squares around the corners!
		# 3) In the beginning, flip as LITTLE pieces as possible. When there are less than 13 squares left, flip as MANY as possible.

	def play_move(self, move): 
		m,n=move[0],move[1]
		for d in range(8):
			i, j = m, n
			if self.check_move(move,d):
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


		

