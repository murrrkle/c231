#Welcome Message
print("Welcome to the Custom Linear Coordinate Distance Solver MkI!\n")

# Entering xA, xB, yA, and yB

xA, yA = float(input("Please enter the x-coordinate of Point A: ")), float(input("Please enter the y-coordinate of Point A: "))

xB, yB = float(input("Please enter the x-coordinate of Point B: ")), float(input("Please enter the y-coordinate of Point B: "))

# Computing the slope and y-intercept of line AB

k = ((yB - yA) / (xB - xA))
b = (yB - (k * xB))

# Let y = 0 for x-intercept

xP, yP = ((0 - b) / k), 0.0

print("\nThe x-intercept of line AB, point P, is ( " + str(xP), str(yP) + " )", sep = " , ")

# Length of AQ: Let x = 0; Redefine the y-intercept as yQ; Use Distance Formula

xQ, yQ = 0.0, b

AQ = ((((xA - xQ) ** 2) + ((yA - yQ) ** 2)) ** 0.5)

print("\nThe length of line AQ is " + str(AQ) + " units.")
