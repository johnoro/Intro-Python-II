from player import Player
from data.rooms import rooms, outside

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
pc = Player(rooms[outside])

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
	args = input('Enter a cardinal direction (n, s, w, e) or q to quit: ')
	args = args.lower().split()
	act = args[0]

	if act == 'q':
		print("\nYou've exited the game. Goodbye.")
		break
	if act in 'nswe':
		try:
			pc.room = rooms[pc.room.getDir(act)]
		except KeyError:
			print("The room doesn't seem to have an exit in that direction.")
	else:
		print("It looks like you didn't enter a cardinal direction.")

print()
