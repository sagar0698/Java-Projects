#This is a physics calculator

operations = [ "Pressure" , "Force" , "Speed" , "Velocity" , "Accelaration" , "Momentum" ]


def pressure():
    print(" ")
    force = int(input("Enter force : "))
    print(" ")
    area = int(input("Enter area : "))
    pressure = force / area
    print(" ")
    print("Pressure is " + str(pressure) + "pascal")

# force function to calculate force
def force():
    print(" ")
    mass = int(input("Enter mass : "))
    print(" ")
    accelaration = int(input("Enter accelaration : "))
    force = mass * accelaration
    print(" ")
    print("Force is " + str(force) + "newton")

# speed func to calculate speed of object
def speed():
    print(" ")
    distance = int(input("Enter distance : "))
    print(" ")
    time = int(input("Enter time taken : "))
    speed = distance / time
    print(" ")
    print("Speed of object is " + str(speed))

# velocity func to calculate velocity of object
def velocity():
    print(" ")
    displacement = int(input("Enter displacement : "))
    print(" ")
    time = int(input("Enter time taken : "))
    velocity = displacement / time
    print(" ")
    print("Velocity of object is " + str(velocity))

# accelaration func to calculate accelaration
def accelaration():
    print(" ")
    initialV = int(input("Enter initial velocity : "))
    print(" ")
    finalV = int(input("Enter final velocity : "))
    print(" ")
    time = int(input("Enter time taken : "))
    acce = (finalV - initialV) / time
    print(" ")
    print("Accelaration is " + str(acce) + "m/s sq.")

# monentum func to calculate momentum
def moment():
    print(" ")
    mass = int(input("Enter mass : "))
    print(" ")
    velocity = int(input("Enter velocity : "))
    print(" ")
    momentum = mass * velocity
    print(" ")
    print("Momentum is " + str(momentum))

while True:
    print(" ")
    print("Hello")
    print(" ")
    startOrEnd = input("Would you like to run this program? Please Enter Start or End: ")
    print(" ")
    if startOrEnd.strip() == "Start" :
        for op in operations:
            print(op)
            print(" ")

        main = input("Which one would you like to solve for: ")
        if main.strip() == "Pressure":
            print(pressure())
            continue
        elif main.strip() == "Force":
            print(force())
            continue
        elif main.strip() == "Speed":
            print(speed())
            continue
        elif main.strip() == "Velocity":
            print(velocity())
            continue
        elif main.strip() == "Accelaration":
            print(accelaration())
            continue
        elif main.strip() == "Momentum":
            print(moment())
            continue
        else :
            print("Invalid operation")
            continue
    elif startOrEnd.strip() == "End":
        print("...Progarm Ended...Have a wonderful day!")
        break
