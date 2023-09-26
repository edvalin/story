name = ""

# Introduction
print("Introduction to Game")

# Ask player for name
name = input("Enter your name: ")

# Define what happens in first room
def firstRoom():
    directions = ["l", "r", "d"]
    print("Describe First Room")

    userInput = ""
    while userInput not in directions:
        print("Select the where to go next: [l]eft/[r]ight/[d]ownward")
        userInput = input()
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