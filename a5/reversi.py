from game import *
from copy import deepcopy
from time import sleep
import sys
from subprocess import PIPE,Popen
from threading import Thread
from queue import Queue,Empty



def ParseEvent() :
	r=receive()
	if r==None:return None,None
	s=[x.rstrip().strip() for x in r.split(":")]
	return s[0],s[1]


def highlight(move):
	send( 'color 255 0 0\n circle %d %d 11\n' % \
		(240+(move[0]+0.5)*40, 100+(move[1]+0.5)*40))


def stone(x,y,turn):
	send('color %d %d %d\n' % \
		(255*(1-turn),255*(1-turn),255*(1-turn)))
	send('fillcircle %d %d %d\n' % \
		(240+(x+0.5)*40, 100+(y+0.5)*40, 17))


def draw(board):
	send('color 20 20 20\n clear\n color 15 15 100\n')
	send( 'button button1 600 20 100 20 "Calculate W:L"')
	send('fillrect %d %d %d %d\n' % (240,100,320,320))
	send('color 0 70 0\n') 
	for i in range(1,8):
		send('line %d %d %d %d\n' %\
			(240+i*40,100, 240+i*40,420))
		send('line %d %d %d %d\n' %\
			(240, 100+i*40, 560, 100+i*40))
	for i in range(8):
		for j in range(8):
			if board[i][j] >= 0:
				stone(i, j, board[i][j])

def makeBoard():
	board = []
	for i in range(8):
		board.append([])
		for j in range(8):
			board[i].append(-1)	 
	board[3][3], board[4][4], board[3][4], board[4][3] = 0,0,1,1
	return board



def _queueqd(ip,q):
	for line in iter(ip.readline,b''):
		q.put(line)
	ip.close()
	
def send(*args):
	s=""
	for a in args:
		s+=str(a)
		if s[-1]!=" ":s+=" "
	if s!="":
		op.write((s[:-1]+"\n").encode('utf-8'))
	else:
		op.write("\n".encode('utf-8'))
	
def receive():
	try:
		return qdq.get_nowait().decode('utf-8')[:-1]
	except Empty:
		return None
def running():
	return qdp.poll()==None


def simulate(numTimes=1000):
	w=0
	b=0
	for i in range(numTimes):
		goesFirst=i&1
		gb=makeBoard()
		sg = Game(gb, goesFirst)
		count = 4
		while count < 64: # max num of stones is 64
			sg.get_moves()
			if sg.moves == []: 
				sg.turn = 1 - sg.turn
				sg.get_moves()
				if sg.moves!= []:
					continue 
				sg.turn = 1 - sg.turn
				break 
			if sg.turn==0:
				mv = sg.select_move()
			else:
				mv= sg.moves[int(len(sg.moves)*random.random())]
			sg.play_move(mv)
			sg.turn=1-sg.turn
			count+=1
		num_white, num_black = sg.final_result()
		if num_white>num_black:w+=1
		if num_black>num_white:b+=1
	return w/b
	
try:
	qdp = Popen("java -jar quickdraw.jar",shell=True,stdout=PIPE,stdin=PIPE)
	op=qdp.stdin
	qdq = Queue()
	qdt = Thread(target=_queueqd,args=(qdp.stdout,qdq))
	qdt.daemon=True
	qdt.start()
except:
	print("quickdraw.jar must be in the same directory as this python script.")
	quit()

send( "mouseclick True\n" )
# initialize the board, get ready for the game 

board =makeBoard()
draw(board) 


# game time, let's play...
# human player is white and moves first

g = Game(board, 0)
count = 4
while count < 64: # max num of stones is 64
	g.get_moves()
	if g.moves == []: 
		g.turn = 1 - g.turn
		g.get_moves()
		if  g.moves!= []:
			continue 
		g.turn = 1 - g.turn
		break 
	if g.turn == 0:
		while running():
			event, val = ParseEvent()
			if event == "MouseClicked":
				val=[ int(x) for x in val.split(",")]
				move = [(val[0]-240)//40, (val[1]-100)//40]
				if move in g.moves: break
			elif event=="ButtonClicked":
				send("colour 20 20 20\nfillrect 600 50 200 50\ncolour 255 255 255")
				send('text "Calculating..." 600 80')
				r=simulate()
				send("colour 20 20 20\nfillrect 600 50 200 50\ncolour 255 255 255")
				send("text ",'"W:L=',r,'"'," 600 80")
	else:
		move = g.select_move()
	stone(move[0], move[1], g.turn)
	highlight(move)
	sleep(1)
	board = deepcopy(g.board)
	g.play_move(move)
	g.turn=1-g.turn
	for i in range(8):
		for j in range(8):
			if board[i][j]!= g.board[i][j]:
				stone(i,j,1-g.turn)
	sleep(1)
	stone(move[0], move[1], 1-g.turn) # redraw to de-highlight
	count += 1


# game over, let's announce the result:

num_white, num_black = g.final_result()
send('color 255 255 255\n')
if num_black > num_white:
	send('text "black wins!" 370 470\n')
elif num_black < num_white:
	send('text "white wins!" 370 470\n')
else:
	send('text "tie!" 390 470\n')
send('text "black:" 325 500\n')
send('text "%d" 375 500\n' % num_black)
send('text "white:" 425 500\n')
send('text "%d" 475 500\n' % num_white)

while running():
	pass
