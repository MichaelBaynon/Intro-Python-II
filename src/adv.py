from room import Room
from player import Player

# Declare all the rooms

room = {

'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", "Pipe Pistol", "Grendade"),


    'foyer': Room("Foyer", "Dim light filters in from the south. Dusty passages run north and east", "Raider's Gear",
                  "Grendade"),


 'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", "FatMan", "Grendade"),


'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", "Institute Pistol", "Grendade"),

'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", "Super Mutant Cowl", "Grendade"),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.


player = Player(input("Character Name: "), room['outside'], items=None)

print(player.current_room)
print(player.current_item)

directions = ["n", "s", "e", "w"]
items = ["Pipe Pistol", "Grenade", "Raider's Gear", "FatMan", "Institute Pistol", "Super Mutant Cowl"]

while True:
    cmd = input(f"What item does {player.name} want?")
    if cmd in items:
        player.pickup(cmd)
    else:
        print("That item is not in this room")

while True:
    cmd = input(f"Will {player.name} travel north[n], south[s], east[e], or west[w]? or quit[q] ").lower()
    if cmd in directions:
        player.travel(cmd)
    elif cmd == "q":
        print(f"\nThanks for playing")
        break
    else:
        print("I did not recognize that command")



# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
