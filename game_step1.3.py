name = ""

# Introduction
print("Introduction to Game")

# Ask player for name
name = input("Enter your name: ")
print("Your name is: " + name)


# Define what happens in first room
def firstRoom():
    print("Describe First Room")
    # Ask player for next move
    userInput = input("Where you want to go next? [l]eft, [r]ight, [u]pwards, [d]ownwards? ")
    print("You are going: " + userInput)

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

# go to exit room
exitRoom()

# go to empty room
emptyRoom()

# go to wand room
wandRoom()