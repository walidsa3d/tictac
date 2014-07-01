#!/usr/bin/env python 

matrix = [[0 for x in xrange(3)] for x in xrange(3)] 

def init():
	for i in xrange(3):
		for j in xrange(3): 
			matrix[i][j] =' '

def player1():
	(x,y)=tuple(int(x.strip()) for x in raw_input("Player 1 (X):").split(','))
	if matrix[x-1][y-1]!= ' ':
		print "Invalid move, try again!.\n"
		player1()  
	else:
		matrix[x-1][y-1] = 'X'

def player2():
	(x,y)=tuple(int(x.strip()) for x in raw_input("Player 2 (O):").split(','))
	if matrix[x-1][y-1]!= ' ':
		print "Invalid move, try again!.\n"
		player2()  
	else:
		matrix[x-1][y-1] = 'O'
def display():
	for t in xrange(3):
		print " %c | %c | %c " %(matrix[t][0],matrix[t][1], matrix [t][2])
		if(t!=2):
			print "\n--------\n"
	print("\n")

def check():
	for i in xrange(3):
			if matrix[i][0]==matrix[i][1] and matrix[i][0]==matrix[i][2]:
			 return matrix[i][0];

	for i in xrange(3):
		if matrix[0][i]==matrix[1][i] and matrix[0][i]==matrix[2][i]:
			return matrix[0][i]

	if matrix[0][0]==matrix[1][1] and matrix[1][1]==matrix[2][2]:
		   return matrix[0][0];

	if matrix[0][2]==matrix[1][1] and matrix[1][1]==matrix[2][0]:
		   return matrix[0][2]

	return ' '
def main():
	print "Tic Tac Toe.\n"
	done =  ' '
	init()
	while done==' ':
		display()
		player1()
		display()
		done = check(); 
		if done!= ' ':
		 break
		player2()
		done = check()
	if done=='X':
		print "Player 1 won!\n"
	else:
		print "Player 2 won!\n"

if __name__ == "__main__":
	main()

	
	

