name = ""

# Introduction
print("Introduction to Game")

# Ask player for name
name = input("Enter your name: ")
print("Your name is: " + name)

# Define what happens in first room
def firstRoom():
    print("Describe First Room")
    
    userInput = input("Where you want to go next? [l]eft, [r]ight, [d]ownwards? ")

    # Add conditional statements
    if userInput == "l":
        exitRoom()
    elif userInput == "r":
        wandRoom()
    elif userInput == "d":
        emptyRoom()
    else: 
        print("Please enter a valid option for the adventure game.") 

# Define what happens in exit room
def exitRoom():
    print("Describe Exit Room")

# Define what happens in empty room
def emptyRoom():
    print("Describe Empty Room")

# Define what happens in wand room
def wandRoom():
    print("Describe Wand Room")

# go to first room
firstRoom()