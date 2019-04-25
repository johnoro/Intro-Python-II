from data.actions import actions, get, drop
from data.commands import commands, inventory, q
from data.characters import pc
from helpers.general import format_list
from helpers.items import names
from adventure.actions import handle_get, handle_drop

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
	args = input('Enter a cardinal direction or q to quit: ')
	args = args.lower().split()
	try:
		act = args[0]
	except IndexError:
		print("It looks like you didn't enter anything parseable.")
		continue

	if len(args) == 2:
		obj = args[1].lower()
		if act in actions[get]:
			handle_get(pc.items, obj, pc.room)
		elif act in actions[drop]:
			handle_drop(pc.room.items, obj, pc)
		else:
			print(f'{act} is not a currently implemented action.')

		continue

	if act in commands[q]:
		print("\nYou've exited the game. Goodbye.")
		break
	if act in 'nswe':
		try:
			pc.move(act)
		except KeyError:
			print("The room doesn't seem to have an exit in that direction.")
	elif act in commands[inventory]:
		print(f'Inventory: {format_list(names(pc.items))}')
	else:
		print("It looks like you didn't enter a cardinal direction.")

print()
