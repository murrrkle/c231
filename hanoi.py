# This program solves the classic Hanoi tower puzzle
# Assume the three piles are numbered 0, 1 and 2 respectively.
# initial state: 4 pieces at pile 0
# end state: 4 pieces at pile 2


def move(a, b):
	print(a, '-->', b)

def hanoi(a, b, k):
	if k > 0:
		c = 3 - a - b
		hanoi(a, c, k-1)
		move(a, b)
		hanoi(c, b, k-1)


hanoi(0, 2, 10)
