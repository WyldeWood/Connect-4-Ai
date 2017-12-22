#############################################################################
# Final Project: Part 1 (Template)
#############################################################################

class Board:
	def __init__(self, rows, cols):
		"""
		Initializes board state for a given number of rows and columns
		(forms a matrix of dimension rows x columns, filled with 0s)

		rows: desired number of rows for this board
		cols: desired number of cols for this board
		"""
		self.rows = rows
		self.cols = cols
		self.state = [[0 for i in xrange(cols)] for i in xrange(rows)] #	addressed as: [row][col]

	def display(self):
		"""
		Displays the current internal board state in the console
		"""
		print"-----------------------------" 			#makes it look nice :)
		for i in range(6):								#makes the board
			for j in range(7):
				print "|", self.state[i][j],
			print "|"
		print"-----------------------------"			#makes it look nice :)
		print "  0   1   2   3   4   5   6"



		# Here's a sample nested loop to get you started:
		#for i in range(6):
		#	for j in range(7):
		#		print self.state[i],[j] #	addressed as: [row][col]
		#	print ""	# just skips a line

	def makeMove(self, column, piece):
		"""
		Finds first unoccupied space in a column and place player's piece there
		Returns True if successful, False if error occurred

		column: column in which to insert piece
		piece: specific value to insert into specified column
		"""
		#if piece != 1 or piece != 2:
		#	return False

		if self.state[0][column] != 0:			#if the column is full return false
			return False 

		else:
			for i in range(self.rows):
				
				if self.state[i][column] != 0:		#if the column isnt full
					self.state[i-1][column] = piece #put the piece in one above the highest filled spot
					return True
				if i == 5:							#when the loop has run all the way to 5 put the piece in
					self.state[5][column] = piece
					return True


	def getPossibleMoves(self):
		"""
		Returns a list of integers (0-6) representing which columns
		still have open slots (can have pieces put in them)
		"""
		listofPossibleMoves = []
		for i in range(7):

			if self.state[0][i] == 0:
				listofPossibleMoves.append(i)

		return listofPossibleMoves
		

	def isGameOver(self):
		"""
		Checks if game is over (if any player has won)
		Returns which player has won if applicable
		Returns 0 if no player has won yet
		"""

		for i in range(6):		# i IS ROWS
			for j in range(7): # j IS COLUMNS
				if self.state[i][j] == 1 or self.state[i][j] == 2:

					if i < self.rows - 3: 		#makes sure there are at least 3 spaces above the current piece
						for r in range(4):
							 if self.state[i+r][j] == self.state[i][j]:      #verticle 4 in a row
								if r == 3:
							 		return self.state[i][j], 'connected 4 vertically and so won the game'
							 else:
							 	break					 		
								
					if j < self.cols - 3:
						for u in range(4):
							#if j == self.cols - 3:
								if self.state[i][j+u] == self.state[i][j]:		#horizontal 4 in a row
									if u ==3:
										return self.state[i][j], 'alligned 4 pieces and takes the prize'
								else:
									break		

					if i < self.rows - 3 and j < self.cols - 3:		
						for d in range(4):
							#if i == self.rows - 3 and j == self.cols - 3:
								if self.state[i+d][j+d] == self.state[i][j]:	#Diagonal 4 in a row up to the right
									if d == 3:
										return self.state[i][j], 'tricked his opponent into a false sense of security and stealthily secured 4 diagonal pieces'
								else:
									break

					if i < self.rows + 3 and j < self.cols - 3:		
						for d in range(4):
							#if i == self.rows - 3 and j == self.cols - 3:
								if self.state[i-d][j+d] == self.state[i][j]:	#Diagonal 4 in a row down to the right
									if d == 3:
										return self.state[i][j], 'undoubtedly won this game with 4 diagonal pieces'
								else:
									break				
						
						
		return 0 	#LEAVE THIS: default to return 0 if nobody has won yet
				# make sure i and j never go out of range
class HumanPlayer:
	def __init__(self, number):
		self.number = number

	def getNextMove(self, board):
		"""
		Returns the integer (0-6) row index of the player's next move

		board: A board state (as defined in your Board class)
		"""
		print "Current Board:"
		#board.display()

		
		#player_next_move = int(raw_input("give me the column in which you want to play")) 	#int makes raw input into and integer
		while True:			#makes sure the input is valid
				try:
					player_next_move = int(raw_input("give me the column in which you want to play"))
					break
				except ValueError:
					print "thats not 0-6 bruh. Try again"

		while not player_next_move in board.getPossibleMoves():
			while True:
				try:
					player_next_move = int(raw_input("give me the column in which you want to play"))
					break
				except ValueError:
					print "thats not 0-6 bruh. Try again"
			#player_next_move = int(raw_input("stop trolling me bro, columns 0-6, pick one")) 
			#while player_next_move != 	#int makes raw input into and integer
																# keep asking
		return player_next_move


#############################################################################
# Final Project: Part 2 (Template)
#
# INSTRUCTIONS:
#
# Copy this template (including the import statement) and paste it below your
#  HumanPlayer and above main in your existing ode from part 1. Follow the
#  instructions in the assignment to continue.
#############################################################################

import random
import Queue
import copy
#AI Player
class AIPlayer:
	def __init__(self, number, piece):
		self.number = number
		self.piece = piece

	def getNextMove(self, board):
		"""
		Returns the integer (0-6) row of the player's next move

		board: A board state (as defined in your Board class)
		"""
		# Random column selection
		# NOTE: Delete all of the code below when you go to fill this in. NONE of it will be reused.
		#possible_moves = board.getPossibleMoves()
		#ai_choice = random.randint(0, len(board.getPossibleMoves())-1)

		#print "AI has chosen: ", possible_moves[ai_choice]

		#return possible_moves[ai_choice]

		move_queue = Queue.PriorityQueue()	#create a priority queue
		for i in board.getPossibleMoves():		#makes sure it only makes a move in a open column
			board_copy = copy.deepcopy(board)	#makes copy of the current board to simulate moves on
			board_copy.makeMove(i, self.number)	#makes the move on that copy
			move_value = self.minimax(board_copy, 5, self.piece, True)	#calls minimax on that new board copy
			move_queue.put((-1 * move_value, i)) #uses the priority queue to get the maximun score that minimax returned
			#print "MOVE", i, "VALUE", move_value

		#var =
		return move_queue.get()[1]
		##print var
		#return var

	def getScoreofList(self, list_of_4_positions):

			score_of_list = 0
			count_of_AI	= list_of_4_positions.count(self.number)
			count_of_player = list_of_4_positions.count(self.piece)
			count_of_0 = list_of_4_positions.count(0)

			if not 0 in list_of_4_positions: #makes sure only groups with only AI pieces and oppenents pieces enter the if statement
				if count_of_AI == 4:
					return score_of_list + 10000	# if there are 4 AI pieces (win state) add 10000 to score of list
				if count_of_AI == 3:
					return score_of_list + 0 # if the list is not all either the AI's piece or the Opponents Piece add 0 to the score
				if count_of_AI == 2:
					return score_of_list + 0 # if the list is not all either the AI's piece or the Opponents Piece add 0 to the score
				if count_of_AI == 1:
					return score_of_list + 0 # if the list is not all either the AI's piece or the Opponents Piece add 0 to the score
				if count_of_player == 4:
					#print list_of_4_positions, "TRIGGERED"
					return score_of_list - 100000 # if there are 4 Opponents pieces (loose state) subtract 10000 to score of list

			if 0 in list_of_4_positions and self.number in list_of_4_positions:#makes sure only groups with only 0's and the AI's pieces enter the if statement
				
				if count_of_AI == 3:
					return score_of_list + 400 # if there are 3 AI pieces in a row add 400 to score 

				if count_of_AI == 2:
					return score_of_list + 75 # if there are 2 AI pieces in a row add 75 to score 

				if count_of_AI == 1:
					return score_of_list + 5 # if there is 1 AI pieces in a row add 5 to score 

			if 0 in list_of_4_positions and self.piece in list_of_4_positions: #makes sure only groups with only 0's and oppenents pieces enter the if statement
				
				if count_of_player == 3: # if there are three opponents pieces in the list subtract 200 from score (1,1,1,0)
					return score_of_list - 200

				if count_of_player == 2:
					return score_of_list - 50 # if there are two opponents pieces  in the list subtract 200 from score (1,0,1,0)

				if count_of_player == 1:
					return score_of_list - 1 # if there is one opponents pieces in the list subtract 200 from score (0,0,1,0)


			#if 0 in list_of_4_positions:
				#print "0 is in list_of_4_positions"
			#if self.piece in list_of_4_positions:						#testing for a broken if statement
				#print "player piece is in list_of_4_positions"
			#if self.number in list_of_4_positions:
				#print "AI piece is in list_of_4_positions"


			if 0 in list_of_4_positions and self.piece in list_of_4_positions and self.number in list_of_4_positions:
				#print "glerp"
				if count_of_AI == 2: # if there are 2 AI pieces in the 4 positions add 30 to the score (2,2,0,1)
					return score_of_list + 30

				if count_of_player == 2: # if there are 2 opponent pieces in the 4 positions subtract 30 from the score (1,2,1,0)
					return score_of_list - 30

				if count_of_0 == 2: # if there are 2 zeros in the 4 positions add 0 to the score (0,2,1,0)
					return score_of_list + 0
			else:
				return score_of_list	#otherwise return the score of the list

	def getBoardScore(self, board):
		"""
		Returns a score value ranking the utility of board to the AI player

		board: A board state (as defined in your Board class)
		"""
		#possibly add scores if more that one good move is possible
		#for i in self.rows():
			#for j in self.cols():
			#while i <= self.rows - 3 and j <= self.cols - 3:
		collective_board_score = 0
		list_of_4_positions = [0, 0, 0, 0]

		for i in range(board.rows):
			for j in range(board.cols):
				if j < board.cols - 3: # makes sure the horizontal set of positions stays on the board (prevents index error)
					#horizontal 4's
					for a in range(0,4): #takes in 4 places on the board
						list_of_4_positions[a] = board.state[i][j+a] # makes sure those pieces are horizontal
					collective_board_score = collective_board_score + self.getScoreofList(list_of_4_positions) #calls getScoreofList on the list of four position
				if i < board.rows -3:
					#verticle 4's
					for a in range(0,4): #takes in 4 places on the board
						list_of_4_positions[a] = board.state[i+a][j] #makes sure pieces are verticle
					collective_board_score = collective_board_score + self.getScoreofList(list_of_4_positions) #calls getScoreofList on the list of four position
				if i < board.rows - 3 and j < board.cols -3:
					#northeast 4's
					for a in range(0,4): #takes in 4 places on the board
						list_of_4_positions[a] = board.state[i-a][j+a] #makes sure pieces are diagonal to the northeast
					collective_board_score = collective_board_score + self.getScoreofList(list_of_4_positions) #calls getScoreofList on the list of four position
					#Southeast 4's
					for a in range(0,4): #takes in 4 places on the board
						list_of_4_positions[a] = board.state[i+a][j+a] #makes sure pieces are diagonal to the south east
					collective_board_score = collective_board_score + self.getScoreofList(list_of_4_positions) #calls getScoreofList on the list of four position

		return collective_board_score

		#return score_of_board_Southeast + score_of_board_Northest + score_of_board_verticles + score_of_board_horizontals

		#for a in range(self.cols):
			#if a 

	def minimax(self, board, depth, piece, mini):
		"""
		Returns a utility score value resulting from exploring board to specified depth

		board: a board state (as defined in your Board class)
		depth: integer representing number of additional times to recur before returning
		mini: indicates current player turn (True = opponent's turn, False otherwise)
		"""
		if board.isGameOver() == 1 or board.isGameOver() == 2 or depth == 0: #minimax will only run of the game isnt over and if the depth is greater than 0
			#if board.isGameOver() > 0:
				#print "LULZ: ", self.getBoardScore(board), "when", board.isGameOver(), "wins"
			return self.getBoardScore(board)
		else:
			list_of_boards = [] #creates list for boards
			list_of_scores = [] #creats list for scores of boards

			for i in board.getPossibleMoves(): #uses only possible moves
				Board_copy = copy.deepcopy(board) #makes copy of board

				if mini:	#if mini is true append the board with the opponants move made in it onto the board list
					list_of_boards.append(Board_copy.makeMove(i, self.piece))
				else:	#otherwise append the board with the AIs move onto the board list
					list_of_boards.append(Board_copy.makeMove(i, self.number))

				scoreofscores = self.minimax(Board_copy, depth - 1, piece, not mini) #recursivly call minimax with in itself to switch it form mini to max each time
				list_of_scores.append(scoreofscores)
				#Board_copy.display()
				#print "I gave the above a", scoreofscores

			if mini == True: #if mini is true (opponents turn) return the smallest value
				#print "MINI:", min(list_of_scores)
				return min(list_of_scores)

			if mini == False:	#if mini is false (AIs turn) Return the biggest score
				#print max(list_of_scores)
				return max(list_of_scores)

def main():
	board = Board(6, 7) #sets board dimensions 
	p1 = HumanPlayer(1)	#sets player 1 as a human
	p2 = AIPlayer(2, 1)	#sets player 2 to AI
	print "Current Board:"
	board.display()		#displays the original board
	
	while board.isGameOver() == 0:				
		if len(board.getPossibleMoves()) == 0:
			print "the game is a tie y'all suck at this"				#its ugly but it works
		player_1s_move = p1.getNextMove(board)							#sets the move made by player 1 = player 1s move
		board.makeMove(player_1s_move, 1)
		board.display()	
									#makes that move and puts a 1 there
		print "AI is divining your demise........"
		if board.isGameOver() != 0:
			break

		if len(board.getPossibleMoves()) == 0:
			print "the game is a tie y'all suck at this"				#its ugly but it works checks if the board isnt full
			break

		player_2s_move = p2.getNextMove(board)							#sets the move made by player 2 = player 2s move
		board.makeMove(player_2s_move, 2)
		print "AI chose", player_2s_move								#makes that move and puts a 1 there
		board.display()
		if len(board.getPossibleMoves()) == 0:
			print "the game is a tie y'all suck at this"				#its ugly but it works
			break
	
	print board.isGameOver()


# Initialization code: No need to change
print "Welcome to Connect Four!"
main()
print "Thanks for playing or losing :("