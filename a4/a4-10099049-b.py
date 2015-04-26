#Computer Science 231, Assignment 4: Drawing Orbital Systems			#Introduction!
#Written By: Bryan Huff		Student ID# 10096604
#Due Date: November 24th 2012
#Excuse some comments, was writing them while bored. Made it more entertaining for me to read/debug the code
#Dictionaries are of the form Planets{Sun: [orbit, period, radius, sattelites, x, y], Moon: etc.etc.}

from math import cos, sin, pi											#For the circles
from sys import argv, exit												#File importing and well, exit

def attributes(line,list):												#Reads the file lines to find what property it applies to, and places it in the properties list
	line = line.strip()
	x = line.split(':')													#No space for you!
	x[-1] = x[-1].strip()
	if 'Orbital Radius' in line: list[0] = x[1]
	elif 'Period' in line: list[1] = x[1]								#Having elif is so much cooler than having a bunch of if statements
	elif 'Radius' in line and 'Orbital' not in line: list[2] = x[1]		#For whatever reason, it would still run this for orbital radius, so I had to add in the not orbital there
	elif 'Satellites' in line: list[3] = x[1]
	
def planet_move(x,y,t,orbit,r,name,scale,period):						#This is the drawing function, calculates position and draws it
	print('colour', 120, 120, 120)										#Orbit = orbital radius, r = radius of planet
	print('circle', x, y, orbit * scale)								#x and y are that of the parent originally
	x = x + (sin(t/period) * (orbit * scale))							#new x and y are the position of the new planet
	y = y + (cos(t/period) * (orbit * scale))
	if r < 1:															#This makes it so you can for sure see the planet
		r = 1
	print('colour', 255,255,255)										#Like an artist, I must pick out my colours. For this, 255, 255, 255 definitely seemed ample
	print('fillcircle', x, y, r)
	print('colour', 0, 255, 0)											#To greentext, you must type > in front of each sentence
	print('text "', name, '"', x, y)
	return x,y															#Return to where you came!
	
def scale_calc(dict,num,pix):											#Calculates the scale of anything wanted
	max = 0																#Pix for pixels, num for entry in dict looking for
	for entry in dict.keys():
		if float(dict[entry][num]) > max:								#What is the entry of the floating dict! :p
			max = float(dict[entry][num]) 
	scale = pix / max
	return scale														#A scale? Are you saying I'm fat?

def draw_planet(dict,planet,parent,time):
	rad_scale = scale_calc(dict,0,275)									#Scaling the radius
	planet_scale = scale_calc(dict,2,15)								#scaling of the planets
	if parent == 'none':												#Base Case
		if planet in dict.keys():
			print('fillcircle', 400, 300, 15)							#Centre planet always the same
			print('colour', 0, 255, 0)
			print('text "', planet, '"', 420, 300)
			dict[planet][4] = 400										#Original x,y
			dict[planet][5] = 300										#^^^^
			if dict[planet][3] != 'none':
				string = dict[planet][3]
				satel = string.split(',')								#It's not a man-purse, it's a satel, like Indiana Jones uses
				for entry in satel:
					draw_planet(dict, entry, planet, time)				#Recursion!
	elif planet in dict.keys():											#Not base case
		if parent in dict.keys():
			if dict[planet][4] == 'none' or dict[planet][5] == 'none':	#For first time to set original x,y
				dict[planet][4], dict[planet][5] = float(dict[planet][0]) * rad_scale, 300
			else:														#Probably an easier way to do this, but works with my data indexing
				dict[planet][4], dict[planet][5] = planet_move(float(dict[parent][4]), float(dict[parent][5]), time, float(dict[planet][0]),float(dict[planet][2]) * planet_scale, planet, rad_scale, float(dict[planet][1]) / (2 * pi))
			if dict[planet][3] != 'none':								#Checks for satellites
				string = dict[planet][3]
				satel = string.split(',')
				for entry in satel:										#Goes through satellites
					entry = entry.strip()
					draw_planet(dict, entry, planet, time)				#We must recurse!
					
def open_file():														#Function that opens the file based off sys.argv
	try:																#making sure file exists
		file = open(argv[1], 'r')
		return file
	except:																#I'm just going with generic error on this one
#		print('Error')													#You don't actually see this with quickdraw open, so there isn't much of a point
		print('text "YOUR FILE IS WRONG!!!!"', 325, 300)				#This seemed like a much more amusing aproach
		exit(2) 														#sys.exit(2) quits the program, but does not quit quickdraw, just to prevent the program from continuing and giving alot of errors
		
file = open_file()
planets = {}															#Who needs oxford or websters when you have planets?
counter = 0																#Variables

while True:																#reading the file
	line = file.readline()
	if 'Root' in line:													#Finding the root object
		line = line.strip()												#Strip!
		root_obj = line.split(':')										#I think it would hurt to split a colon
		root = root_obj[-1]												#This will always be the object since it is after the colon
		root = root.strip()
	elif 'Object' in line:												#Finds each object in file, and sets it as a dictionary entry
		line = line.strip()
		obj = line.split(':')
		obj[-1] = obj[-1].strip()
		properties = ['none','none','none','none','none','none']		#Sets the properties that goes with each dict entry
		if obj[-1] == root:
			properties[4], properties[5] = 400, 300
		for line in file:												#After finding an object, going through the properties until a blank line is found
			if line in ['\n', '\r\n']:									#This was needed to read blank line in windows. if not line did not work when windows would read a file
				break													#Have a break, Have a Kit-kat
			else:
				attributes(line,properties)
				planets[obj[-1]] = properties							#Makes dict entry with a properties list
	elif not line:														#Just a safecheck for finding the end of the file
		counter += 1
		if counter == 5:												#Used lists in my dictionaries because I found it easier to index, and easier to find objects
			break														#Want dictionary such that {'Moon': [orbit, period, radius, sattelites, x, y]

file.close()															#Closing file
time = 100000000																#Variables, but just one
print('graphicsFlush false')											#Don't flush the graphics
while True:
	print('colour', 0, 0, 0)											#For smooth animation in quickdraw
	print('clear')														#Pretty sure black is opaque, not clear
	print('colour', 255, 255, 255)
	draw_planet(planets, root, 'none',time)								#The recursive function
	time += 0.05														#So it changes
	print('refresh')													#F5 F5 F5 F5 F5 F5 F5 F5 F5 F5 F5
