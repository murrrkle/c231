# CPSC 231 ASSIGNMENT TWO PART 2: Ball and Spring in Two Dimensions         Coded by 10099049; Michael Hung

########################################## variable definitions ###########################################

l = 200.0       # length of the spring at equilibrium
k = 1.0         # spring constant
g = 9.8         # acceleration due to gravity
t = 0.02        # time interval
m = 10.0        # mass of the ball
vx = 2.0        # initial horizontal velocity of the ball
vy = 0.0        # initial vertical velocity of the ball

xB = 200.0      # initial horizontal position of ball
yB = 300.0      # initial vertical position of ball

xS = 20.0       # horizontal position of fixed end of spring
yS = 20.0       # vertical position of fixed end of spring

timer = 5000   # timer to end the loop

########################################### function definitions ###########################################

def force_g(m, g):                                  # Calculates the force of gravity
    return m * g

def d_new(position, v, t):                          # Updates the position of the ball
    return position + v * t

def length_spr(xB, yB, xS, yS):                       # Updates the length of the spring
    x_change = xB - xS
    y_change = yB - yS
    l_new = (x_change ** 2 + y_change ** 2) ** 0.5
    return l_new

def force_dir(position, spring_position, l):        # Updates the direction of force
    return (position - spring_position) / l

def force_spr(k, l, l_new, xy_dir):              # Updates the force exerted by the spring
    return -k * (l_new - l) * xy_dir

########################################### animating the ball ############################################

print("graphicsflush False")

while timer > 0:

    l_new = length_spr(xB, yB, xS, yS)

    Fnet_x = force_spr(k, l, l_new, force_dir(xB, xS, l))
    Fnet_y = force_spr(k, l, l_new, force_dir(yB, yS, l)) + force_g(m, g)

    vx += (Fnet_x / m) * t
    vy += (Fnet_y / m) * t

    xB += vx * t
    yB += vy * t

    timer -= 1
    
    print("color 0 0 0")
    print("clear")
    
    print("color 200 255 155")
    print("line 0 10 1000 10")
    
    print("color 100 100 100")
    print("line", 400, 11, xB + 400, yB)
    
    print("color 255 0 0")
    print("fillcircle", xB + 400, yB, "20")
    
    print("refresh")
