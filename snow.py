# To run, type: python snow.py 5 | java -jar quickdraw.jar

from sys import argv

def l_turn(degree):
        print('turtleturn left', degree,  't')

def r_turn(degree):
        print('turtleturn right', degree, 't')

def f(step):
        print('turtlemove forward', step, 't')


def flake(level, step):
    if level == 1: f(step)
    else:
        flake(level-1,step/3)
        r_turn(60)
        flake(level-1,step/3)
        l_turn(120)
        flake(level-1,step/3)
        r_turn(60)
        flake(level-1,step/3)
	

step = 450.0
level = int(argv[1])
print('turtlecreate', 500, 500, 't')
flake(level, step)
l_turn(120)
flake(level, step)
l_turn(120)
flake(level, step)
