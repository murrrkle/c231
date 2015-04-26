# CPSC 231 ASSIGNMENT TWO PART 1: Ball and Spring in One Dimension         Coded by 10099049; Michael Hung


########################################### variable definitions ##########################################


l = 100.0                           # length of the spring at equilibrium
k = 1.0                             # spring constant
g = 9.8                             # acceleration due to gravity
t = 0.03                            # time interval
m = 10.0                            # mass of the ball
yB = 100.0                          # initial vertical position of the ball
v = 2.0                             # initial velocity of the ball

timer = 10000                       # timer countdown to end the looop


########################################### function definitions ##########################################


def force_g(m, g, k, yB, l):        # Calculates the force of gravity
    return m * g - k * (yB - l)

def yB_new(yB, v, t):               # Update position
    return yB + v * t

def v_new(v, Fg, m, t):             # Update velocity
    return v + (Fg/m) * t


########################################### animating the ball #############################################

print("graphicsflush False")


while timer > 0:

    Fg = force_g(m, g, k, yB, l)
    v = v_new(v, Fg, m, t)
    
    yB = yB_new(yB, v, t)

    timer -= 1

    print("color 0 0 0")
    print("clear")
    
    print("color 155 155 55")
    print("line 0 10 1000 10")
    
    print("color 100 100 100")
    print("line 400 10 400", yB)
    
    print("color 255 0 0")
    print("fillcircle 400", yB, "20")
    
    print("refresh")


