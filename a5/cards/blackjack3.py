import random
#from subprocess import Popen, PIPE
from q import *
from time import sleep


class Card:
	def __init__(self, suit='club', rank ='A'):
		self.suit = suit
		self.rank = rank
	def __str__(self):
		return self.suit + '-' + self.rank

class Deck:
	def __init__(self):
		self.cards = []
		for suit in ['club','spade','heart','diamond']:
			for rank in ['A','2','3','4','5','6','7','8', \
				'9','10','J','Q','K']:
				self.cards += [Card(suit,rank)]

	def shuffle(self):
		for i in range(len(self.cards)):
			j = random.randrange(i, len(self.cards))
			self.cards[i],self.cards[j] = self.cards[j],self.cards[i]
		
	def deal(self):
		return self.cards.pop()

class Hand:
	def __init__(self, cards = [], displayed=0):
		self.cards = cards
		self.displayed = displayed

	def get_card(self, card):
		self.cards += [card]
	
	def eval(self):
		score = 0
		has_A = False
		for card in self.cards:
			if card.rank in ['J','Q','K']:
				score += 10
			elif card.rank == 'A':
				score += 1
				has_A = True
			else:
				score += int(card.rank)
		if has_A:
			if score <= 11: score += 10
		if score > 21: score = 0
		return score		

	def want_more(self):
		if self.eval() > 16 or self.eval() == 0: return False
		else: return True

def display(hands):
    for i in range(2):
        for j in range(hands[i].displayed, len(hands[i].cards)):
            s = hands[i].cards[j].__str__()
            send('loadimage %s.png %s\n' % (s, s))
            send('drawimage %d %d %s\n' % (100+j*80, 100+200*i, s))
            hands[i].displayed = len(hands[i].cards) 


def ParseEvent() :
    r=receive()
    if r==None:return None,None
    s=[x.rstrip().strip() for x in r.split(":")]
    return s[0],[ int(x) for x in s[1].split(",")]


deck = Deck()
deck.shuffle()
hands = [Hand([deck.deal()]+[deck.deal()])] + \
	[Hand([deck.deal()]+[deck.deal()])]
display(hands)

send( "mouseclick True\n" )
send( "mousedrag True\n" )
send( "keyevents True\n" )
send( "windowevents True\n" )

send("color 30 20 60\n fillrect 650 100 100 60\n" )
send("color 255 255 255\n text HIT 690 135\n")
send("color 30 20 60\n fillrect 650 250 100 60\n" )
send("color 255 255 255\n text STAND 675 285\n")

while True:
	event, val = ParseEvent()
	if event == "MouseClicked":
		x, y = val[0], val[1]
		if 650<x<750:
			if 100<y<160: 
				hands[0].get_card(deck.deal())
				display(hands)
			if 250<y<310: break
	
while hands[1].want_more():
	hands[1].get_card(deck.deal())
	display(hands)
	sleep(1)

if hands[0].eval() > hands[1].eval():
	send("color 255 255 255\n text YouWin! 350 500\n")
else:
	send("color 255 255 255\n text DealerWins! 350 500\n")

