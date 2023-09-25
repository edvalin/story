name = ""

print("Introduction to Game")
name = input("Enter your name: ")

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


def exitRoom():
    directions = ["u", "r"]
    print("Describe Exit Room")

    userInput = ""
    while userInput not in directions:
        print("What are your next moves: [u]pward/[r]ight")
        userInput = input()
        if userInput == "u":
            print("Congratulate on successfull exit")
        elif userInput == "r":
            firstRoom()
        else: 
            print("Please enter a valid option for the adventure game.")   

def emptyRoom():
    directions = ["u"]
    print("Describe Empty Room")

    userInput = ""
    while userInput not in directions:
        print("There is only one door in this room, you can only go: [u]pward")
        userInput = input()
        if userInput == "u":
            firstRoom()
        else: 
            print("Please enter a valid option for the adventure game.") 

def wandRoom():
    directions = ["l"]
    print("Describe Wand Room")

    userInput = ""
    while userInput not in directions:
        print("There is only one door in this room, you can only go: [l]eft")
        userInput = input()
        if userInput == "l":
            firstRoom()
        else: 
            print("Please enter a valid option for the adventure game.")  


firstRoom()