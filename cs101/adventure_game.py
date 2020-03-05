# Purpose: Adventure Game
# Date: 3/2/2020
# Author: Zach Cooper

###### IMPORT MODULES ######
import random

######## FUNCTIONS #########

# menu function
# 
def menu(l, q):
    """ 
    param 1: list to iterate output from
    param 2: question to ask user
    asks user what they want to inspect first
    """
    for i in l:
        print(1 + l.index(i), i)
    return int(input(q))


###### END FUNCTIONS ########

if __name__ == "__main__":
    # beginning prompt
    print("Last night, you went to sleep in your own home.")
    print("Now, you wake up in a locked room.")
    print("Could there be a key hidden somewhere?")
    print("In the room, you can see:")

    # list of items in the room
    items = ["backpack", "painting", "vase", "bowl", "door"]

    # generate random number for key location
    key_location = random.randint(1,4)

    # key not found variables
    key_found = "No"
    loop = 1

    # call menu
    # menu(items, "What do you want to inspect?")

    # display the menu until the key is found
    while loop == 1:
        choice = menu(items,"What do you want to inspect?")

        print("")

        if choice < 5:
            if choice == key_location:
                print("You found a small key in the", items[choice - 1])
                key_found = "Yes"
            else:
                print("You found nothing in the ", items[choice - 1])
        elif choice == 5:
            if key_found == "Yes":
                loop = 0

                print("You insert the key in the keyhole and turn it.")
            else:
                print("The door is locked. You need to find the key.")
        else:
            print("Choose a number less than 6.")
    
    print("You open the door to your freedom.")