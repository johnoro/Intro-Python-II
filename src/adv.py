from room import Room
from player import Player
from item import Item

# Declare all the rooms
outside = 'outside'
foyer = 'foyer'
overlook = 'overlook'
narrow = 'narrow'
treasure = 'treasure'
room = {
	outside: Room(outside, 'Outside Cave Entrance',
								'North of you, the cave mount beckons.'),
	foyer: Room(foyer, 'Foyer', '''Dim light filters in from the south. Dusty
passages run north and east.'''),
	overlook: Room(overlook, 'Grand Overlook', '''A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.'''),
	narrow: Room(narrow, 'Narrow Passage', '''The narrow passage bends here from west
to north. The smell of gold permeates the air.'''),
	treasure: Room(treasure, 'Treasure Chamber', '''You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.'''),
}

# Link rooms together
room[outside].setDir('n', foyer)
room[foyer].setDir('s', outside)
room[foyer].setDir('n', overlook)
room[foyer].setDir('e', narrow)
room[overlook].setDir('w', foyer)
room[narrow].setDir('w', foyer)
room[narrow].setDir('n', treasure)
room[treasure].setDir('s', narrow)

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
pc = Player(room[outside])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters 'q', quit the game.
while True:
	print(f'\n{pc.room}')
	print(pc.room.description)
	act = input('Enter a cardinal direction (n, s, w, e) or q to quit: ')
	if act == 'q':
		print("\nYou've exited the game. Goodbye.")
		break
	if act in 'nswe':
		try:
			pc.room = room[pc.room.getDir(act)]
		except KeyError:
			print("The room doesn't seem to have an exit in that direction.")
	else:
		print("It looks like you didn't enter a cardinal direction.")

print()
