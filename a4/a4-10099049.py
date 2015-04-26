import math
from sys import argv

file = open(argv[1], 'r').readlines()


print(file)

def dictmake(file):
    system = {}
    orbital_r = []
    radius = []
    period = []
    satellites = []
    
    for line in file:
        
        line = (line.strip()).split(': ')

        if line[0] == 'RootObject':
            rootobject = line[1]
            
        elif line[0] == 'Object':
            system[line[1]] = {'Orbital Radius': '', 'Radius': '','Period': '', 'Satellites': ''}
            
        elif line[0] == 'Orbital Radius':
            orbital_r.append(float(line[1]))
            
        elif line[0] == 'Radius':
            radius.append(float(line[1]))
            
        elif line[0] == 'Period':
            period.append(float(line[1]))
            
        elif line[0] == 'Satellites':
            satellites.append(line[1].split(','))

        elif line == '' or '\n':
            
            if len(satellites) <= len(system):
                satellites.append('')
                
            if len(period) < len(system):
                period.append('')


        print(line)

    systemlist = list(system)

    

    for i in system.keys():
        system[i]['Orbital Radius'] = orbital_r[systemlist.index(i)]
        system[i]['Radius'] = radius[systemlist.index(i)]
        system[i]['Period'] = period[systemlist.index(i)]
#        system[i]['Satellites'] = satellites[systemlist.index(i)]
        
        

    print(system, satellites, period)

def ratio(orbital_r):
    return 290//max(orbital_r)

def draw(body, x, y):
    return None

    
        
dictmake(file)

