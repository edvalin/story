name = ""
haveWand = False

isFirstRoomVisited = False
isExitRoomVisited = False
isEmptyRoomVisited = False
isWandRoomVisited = False


print("Introduction to Game")
name = input("Enter your name: ")

def firstRoom():
    directions = ["l", "r", "d"]
    global isFirstRoomVisited
    if isFirstRoomVisited:
       print("you are back to the first room you have started in")
    else:
        print("Describe First Room")
        isFirstRoomVisited = True

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
    global isExitRoomVisited
    global haveWand

    if isExitRoomVisited:
        print("You are back in the room with the exit")
    else:   
        print("Describe Exit Room")
        isExitRoomVisited = True

    userInput = ""
    while userInput not in directions:
        print("What are your next moves: [u]pward/[r]ight")
        userInput = input()
        if userInput == "u":
            if haveWand:
                print("Congratulate on successfull exit")
            else:
                print("Suggest to visit other rooms")
                userInput = ""
        elif userInput == "r":
            firstRoom()
        else: 
            print("Please enter a valid option for the adventure game.")   

def emptyRoom():
    directions = ["u"]
    global isEmptyRoomVisited

    if isEmptyRoomVisited:
        print("You are back in the empty room")
    else:   
        print("Describe Empty Room")
        isEmptyRoomVisited = True

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
    global isWandRoomVisited
    global haveWand 

    if isWandRoomVisited:
        print("You are back in the wand room")
    else:   
        print("Describe Wand Room")
        isWandRoomVisited = True
        haveWand = True

    userInput = ""
    while userInput not in directions:
        print("There is only one door in this room, you can only go: [l]eft")
        userInput = input()
        if userInput == "l":
            firstRoom()
        else: 
            print("Please enter a valid option for the adventure game.")  


firstRoom()