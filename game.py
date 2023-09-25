import time

name = ""
haveWand = False

isFirstRoomVisited = False
isExitRoomVisited = False
isEmptyRoomVisited = False
isWandRoomVisited = False

def pause():
   time.sleep(5)
   print("")


print("Harry, Hermione, and Ron, known for their adventurous spirit, had landed themselves in trouble once again. This time, you were right there with them, trapped in a dimly lit dungeon.")
pause()
print("As you tried to get your bearings in the eerie darkness, the trio looked equally bewildered. Ron, with his fiery red hair and freckles, turned to you with a friendly smile. His voice broke the silence.")
pause()
print("\"Hi, my name is Ron,\" he said, extending a hand towards you. \"What's your name?\"")

name = input("Enter your name: ")

print("\"Nice to meet you, Ron,\" you replied, shaking his hand. \"I'm "+ name +". Let's try to get out of here. Any idea how we ended up in this dungeon?\"")
pause()
print("Ron scratched his head, his expression a mix of concern and curiosity.")
pause()
print("\"Honestly, I'm not entirely sure. It's been a strange day, even by our standards. But don't worry, we've faced worse odds before. We'll figure it out together.\"")
pause()
print("With newfound determination and the famous trio by your side, you set out to unravel the mystery of the dungeon and find a way to escape the perilous situation.")


def firstRoom():
    directions = ["l", "r", "d"]
    global isFirstRoomVisited
    if isFirstRoomVisited:
       print("you are back to the first room you have started in")
    else:
        print("The group decided to thoroughly explore the room before choosing a door. In the dim torchlight, they noticed an enormous tapestry depicting a majestic phoenix. The room was otherwise sparse, with three identical wooden doors along the stone walls. The trio gathered around the doors, searching for clues.")
        pause()
        print("Facing a tough decision with no clear indication, you had three paths to choose from - left, right, and downward. The group awaited your decision on which door to open next.")
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
        pause()
    else:   
        print("As you entered the next room, you found yourselves in a much smaller and dimly lit chamber. This time, there was only a single door on the right side, obstructed by a pile of heavy, seemingly immovable objects. ")
        pause()
        print("The room was filled with a sense of mystery, and your curiosity drove you to examine the pile of obstructions. It appeared to be a jumble of ancient crates, barrels, and large stones, stacked haphazardly to block the passage. In the dim light, you could barely make out faded labels on some of the crates, hinting at forgotten contents. Looking closer you can see through the gap in a door the daylight. ")
        pause()
        print("Ron stepped forward, scratching his head. \" It must be an exit\" he remarked.")
        pause()
        print("Harry scanned the room, his eyes narrowing. \"We should check this room carefully. There might be something here that can help us move these obstructions.\"")
        pause()
        print("Hermione, always quick with a solution, said, \"I remember reading about levitation spells in one of my books. If one of us can perform it, we might be able to clear the path.\"")
        pause()
        print("As you brainstormed ways to clear the path, an unsettling realization dawned upon the group: none of you had your wands. The absence of your magical instruments left you feeling vulnerable and somewhat exposed in this strange, enchanted dungeon.")
        isExitRoomVisited = True

    userInput = ""
    while userInput not in directions:
        print("What are your next moves: [u]pward/[r]ight")
        userInput = input()
        if userInput == "u":
            if haveWand:
                print("The pile of crates, barrels, and stones still stood as a formidable barrier, but now you had a wand that might hold the key to clearing the path.")
                pause()
                print("Ron, eager to put the wand to use, stepped forward with determination. He pointed the wand at the obstructing objects and confidently exclaimed, \"Leviosa!\"")
                pause()
                print("However, instead of the desired effect of the objects levitating and clearing the way, nothing happened. The pile remained unmoved, and the room was filled with a tense silence.")
                pause()
                print("Hermione, ever the expert, stepped in to correct Ron. \"It's pronounced 'Lev-i-o-sa,' Ron, not 'Leviosa.' Here, let me show you.\" She took the wand from him and demonstrated the correct pronunciation, gracefully swishing it through the air as she chanted, \"Lev-i-o-sa.\"")
                pause()
                print("As Hermione's spell took effect, the objects began to levitate one by one, floating gently to the side to create a clear path through the doorway. Ron watched in awe as Hermione effortlessly manipulated the objects with her wand.")
                pause()
                print("Ron scratched his head, his face turning slightly red. \"Right, 'Lev-i-o-sa.' Got it.\"")
                pause()
                print("With the path now cleared, you open the door and escape the dungeon.")
                pause()
                print("\"Thanks!\" "+ name + " shouts Harry and you all step outside")

            else:
                print("Doors are blocked. Explore other rooms. Maybe you will find something that will help you to escape the dungeon")
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
        pause()
    else:   
        print("As you entered the room beyond it, you found yourselves in a surprisingly empty chamber. The room was devoid of any notable features or objects.")
        pause()
        print("Harry let out a sigh of frustration. \"Well, that was anticlimactic. It seems like this room leads us nowhere.\"")
        pause()
        print("Hermione, the eternal optimist, tried to find meaning in the emptiness. \"Perhaps it's a hint, or a test of our patience. Maybe we need to be more thorough in our search.\"")
        pause()
        print("Ron, ever the pragmatist, chimed in, \"Or it could just be a dead end, and we should keep exploring\"")
        pause()
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
        pause()
    else:   
        print("This room was unlike any other you had encountered in the dungeon. It was grand and opulent, with towering pillars and walls adorned with shimmering tapestries depicting ancient magical battles and legendary creatures. In the center of the room, atop a magnificent stone pedestal, rested a wand, bathed in a soft, otherworldly light.")
        pause()
        print("\"It is a wand!\" Hermione exclaimed, her eyes sparkling with delight as she held it up for the others to see. \"This could make things much easier.\"")
        pause()
        print("The wand was old and worn, its wood polished from years of use, but it still retained a hint of magical energy. The trio exchanged glances, a mix of relief and anticipation in their expressions.")
        pause()
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