# text-based adventure

# scenario = print('You are walking through a dark forest ')

item = input(f"You are walking through a dark forest and find two item: " + "a MATCH and a FLASHLIGHT. " + "Which one do you want to pick up? ")

# Match
# item = input('Enter item: ')

# scenario for match
if item == "match": 
    match = input("You pick up the match and strike it, and for an instant, the forest around you is illuminated. You see a large grizzly bear, and then the match burns out. Do you want to RUN, or HIDE behind a tree?") 

    print() # space

    if match == "run":
        print("Run run run")

    elif match == "hide":
        print("Hide hide hide")

# scenario for flashlight
if item == "flashlight":
    flashlight = input("You pick up the flashlight and turn it on. You see the pathway lit up in front of you, but you thought you also heard something off to the side. Do you want to FOLLOW the path or LOOK in the trees for the thing that made the noise?") 

    print() # space

    if flashlight == "follow":
        print("Follow follow follow")

    elif flashlight == "look":
        print("Look look look")







    
