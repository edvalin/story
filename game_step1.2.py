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

# go to first room
firstRoom()

# go to first room again
firstRoom()