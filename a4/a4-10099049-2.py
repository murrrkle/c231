# CPSC 231 Assignment 4                                             10099049; Michael Hung

import math                             # for trigonometric functions and pi
from sys import argv                    # for file import outside of Python

def dictmake(file):                     # Creates the dictionary for use in other functions NOTE: I never did get this to work. The program is incomplete as a result.
    system = {}
    for line in file:
        line = (line.strip()).split(': ') # This loop creates a dictionary in the form {'Sun': {}, 'Moon': {}, etc} . However, I couldn't figure out how to put the attributes into each sub dictionary.
        if line[0] == 'RootObject':
            rootobject = line[-1]

        =
            
        if line[0] == 'Object':
            system[line[-1]] = {}
           
    print(system)


file = open(argv[1], 'r').readlines()
dictmake(file)

