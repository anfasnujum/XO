import random
import copy

#Define the class
class XO:
	def __init__(self):
		self.board = [[0,0,0],[0,0,0],[0,0,0]]
		self.turn = 1

	def input(self,row,column):
		if self.board[row][column] == 0:
			if self.turn == 1:
				self.board[row][column] = 1
			elif self.turn == -1:
				self.board[row][column] = -1
			self.changeturn()
			return True
		else:
			return False

	def check(self):
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

	def copy(self):
		return self

	def show(self):
		for i in range(0,3):
			print(self.board[i])

	def changeturn(self):
		if self.turn == 1:
			self.turn = -1
		else:
			self.turn = 1

#Function to generate a random point
def generatepoint():
	row = random.randrange(0,3)
	col = random.randrange(0,3)
	point = [row,col]
	return point

#Function to play game and return if the first player wins
def playgame(board):
	tempboard = copy.deepcopy(board)
	turn = board.turn
	no_of_turns = 0
	for i in range(0,3):
		no_of_turns += tempboard.board[i].count(0)
	i = 0

	while i ==0:
		point1 = generatepoint()
		if tempboard.input(point1[0],point1[1]):
			i = 1
	#		tempboard.changeturn()


	for i in range(0,no_of_turns-1):
		#insert
		j=0
		while j==0:
			point = generatepoint()
			if tempboard.input(point[0],point[1]):
				j = 1
	#			tempboard.changeturn()
		if tempboard.check() == turn:
			return point1
	return None

def compplay(board,accuracy):
	scoreboard = [[0,0,0],[0,0,0],[0,0,0]]
	for i in range(0,accuracy):
		point = playgame(board)
		if point != None:
			scoreboard[point[0]][point[1]] += 1

	max =[[0,0],0]
	for i in range(0,3):
		for j in range(0,3):
			if scoreboard[i][j] >= max[1]:
				max[0][0]=i
				max[0][1]=j
				max[1]=scoreboard[i][j]
	return max[0]

def playerinput():
	point =[0,0]
	pointin = input("Enter the row and column seperated by space:")
	point = list(map(int,pointin.split(" ")))
	if point[0] not in range(0,3):
		if point[1] not in range(0,3):
			point = playerinput()
	return point


#Start game
accuracy = int(input("Input an accuracy:"))
playercoin = str(input("Pick a coin (0/X):"))

if playercoin == "X":
	playerturn = 1
elif playercoin == "O":
	playerturn = -1


board = XO()
board.show()
print(board.turn)
print("_______________________")
point = [0,0]

	#first turn
if playercoin == "O":
	print("Computer's Turn:")
	point = compplay(board,accuracy)
	board.input(point[0],point[1])
	print(board.turn)
	board.show()
	print("Computer played:",point)

elif playercoin == "X":
	print("Your Turn:")
	point = playerinput()
	board.input(point[0],point[1])
	print(board.turn)
	board.show()
	print("You played:",point)
print("_______________________")

for i in range(0,7):
	if board.turn == playerturn:
		print("Your Turn:")
		k=0
		while k == 0:
			point = playerinput()
			if board.input(point[0],point[1]):
				k = 1
		print("You played:",point)

	else:
		print("Computer's Turn:")
		point = compplay(board,accuracy)
		k=0
		while k ==0:
			if board.input(point[0],point[1]):
				k=1
		print("Computer played:",point)
	print(board.turn)
	board.show()
	print("_______________________")
	if board.check() == playerturn:
		print("You WON!")
		break
	elif board.check() == -1*playerturn:
		print("You LOST!")
		break



















                
