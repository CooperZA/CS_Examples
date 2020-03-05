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


