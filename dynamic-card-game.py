import numpy as np

# naive solution to question: A casino offers a card game with the standard 52 cards (26 red, 26 black). 
# The cards are thoroughly shuffled and the dealer draws cards one by one. 
# (Drawn cards are not returned to the deck). You can ask the dealer to stop at any time you like. 
# For each red card drawn, you win 1 dollar; for each black card drawn, you lose 1 dollar. 
# What is the optimal stopping rule in terms of maximizing expected payoff and how much are you willing to pay for this game?

# base case dcg(0,r) = 0 rather than -r, because you can always choose to end the game when you find the payoff is negative.

# def dcg(b,r):
# 	if b == 0:
# 		return 0
# 	elif r == 0:
# 		return b
# 	else:
# 		return max((b-r), (((b/(b+r))*dcg(b-1, r))+((r/(b+r))*dcg(b, r-1))))

# print(dcg(3, 4))

# 1 red, 

# matrix = np.zeros((27,27))
# #print(matrix)
# for i in range(len(matrix[0])):
# 	matrix[0][i] = i

# for b in range(1, 27):
# 	for r in range(1, 27):
# 		matrix[r][b] = max(b - r, (((b/(b+r))*matrix[r][b-1])+((r/(b+r))*matrix[r-1][b])))

# print(matrix)

def dcg(black, red):
	matrix =  np.zeros((red+1,black+1))
	for i in range(len(matrix[0])):
		matrix[0][i] = i
	for b in range(1, black+1):
		for r in range(1, red+1):
			matrix[r][b] = max(b - r, (((b/(b+r))*matrix[r][b-1])+((r/(b+r))*matrix[r-1][b])))
	return matrix[red][black]

print(dcg(26, 26))
