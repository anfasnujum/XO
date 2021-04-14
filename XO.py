class XO:
	def __init__(self,turn):
		self.board = [[0,0,0],[0,0,0],[0,0,0]]
		self.turn = str(turn)

	def input(row,column,coin):
		if self.board[index] != None:
			if coin == "X":
				self.board[index] = 1
			elif coin == "O":
				self.board[index] = 0
			self.changeturn()
			return 1
		else:
			self.changeturn()
			return 0

	def check():
		# rows
		for i in range(0,3):
			sum = 0
			for j in range(0,3):
				sum = sum + self.board[i][j]
			if sum == 3:
				return 1
			elif sum == -3:
				return -1
		#columns
		for i in range(0,3):
			sum = 0
			for j in range(0,3):
				sum = sum + self.board[j][i]
			if sum == 3:
				return 1
			elif sum == -3:
				return -1
		# diagonals

		leftdia = self.board[0][0] + self.board[1][1] + self.board[2][2]
		rightdia = self.board[0][2] + self.board[1][1] + self.board[2][0]

		if leftdia == 3 or rightdia == 3:
			return 1
		elif leftdia == -3 or rightdia == -3:
			return -1 

		return 0

	def show():
		print("nooo")
		for i in range(0,3):
			print("hI")
			print(self.board[i])

	def turnout():
		return turnout

	def changeturn():
		if self.turnout == 1:
			self.turnout = -1
		else:
			self.turnout == 1

start = str(input("Who begins the game? (0/X):"))

board = XO(start)
print("hEY")
print(board.show())
print("bYE")
print(board.turnout)







                
