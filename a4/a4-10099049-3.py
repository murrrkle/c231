import math
from sys import argv

file = open(argv[1], 'r')



def dictmake(file):

    system = {}

    for i in file:
        line = (i.strip()).split(': ')
    
        if line[0] == 'RootObject':
            rootobject = line[1]
            
        if line[0] == 'Object':
            system[line[1]] = {'Orbital Radius': '', 'Radius': '','Period': '', 'Satellites': ''}

    for i in system:
        s = file.readlines(5)
            
            

            
        print(s)


dictmake(file)
