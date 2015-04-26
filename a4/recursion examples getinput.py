

# The program structure should first getInput(), then it whould Animate() --> draw(s, x, y)

system = {'Uranus':{'Orbital Radius': 453572956, 'Radius': 2555900, 'Period':30799, 'Satellites':['Puck', 'Miranda', 'Ariel', 'Umbriel', 'Titania', 'Oberon']}, 'Earth':{}, 'Moon':{}}

# The main dictionary system should include every satellite as a key, and each of their information as their own dictionaries - i.e. dictionaries within a dictionary.



def getInput(x): #Get the input from file and go through each line.
                #Say the current line is e, then you e.split(': ')
                #if L[0] = ...: system[curent_skybody][L[0]] = L[1].
                #For L[1], you need to do type conversion first.
                #if L[0] == 'Object': curent sky_body = L[1], system[L[1]] = {}
                # e.split(', ') for satellites
                # if L[0] == 'Root...': rootobject

def dataProcess(): # Get the biggest orbital radius, ratio = 290/max_radius

def draw(s, x, y): #Draw skybody s (fill circle using radius).
                            #Go through each satellite t of s.
                                #Draw orbit of t (circle using orbital radius)
                                #Draw (t, x_t, y_t)
def animation():
    # t += 1. 0.1
    # t / period * 2*math.pi gives the angle
    # draw(rootobject)
