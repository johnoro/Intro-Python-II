from player import Player
from data.rooms import rooms, outside
from data.actions import actions, get, drop
from data.commands import commands, inventory, q
from helpers.general import formatList
from helpers.items import names, move

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
	try:
		act = args[0]
	except IndexError:
		print("It looks like you didn't enter anything parseable.")
		continue

	if len(args) == 2:
		obj = args[1].lower()
		if act in actions[get]:
			removed = pc.room.removeItem(obj)
			move(pc.items, removed, obj)
		elif act in actions[drop]:
			removed = pc.removeItem(obj)
			move(pc.room.items, removed, obj)
		else:
			print(f'{act} is not a currently implemented action.')

		continue

	if act in commands[q]:
		print("\nYou've exited the game. Goodbye.")
		break
	if act in 'nswe':
		try:
			pc.room = rooms[pc.room.getDir(act)]
		except KeyError:
			print("The room doesn't seem to have an exit in that direction.")
	elif act in commands[inventory]:
		print(f'Inventory: {formatList(names(pc.items))}')
	else:
		print("It looks like you didn't enter a cardinal direction.")

print()
