from data.actions import actions, get, drop, attack, inspect
from data.commands import commands, inventory, _quit, _help
from data.characters import pc
from helpers.general import format_list, names, wrap, flatten_object
from adventure.actions import handle_get, handle_drop, handle_attack, handle_inspect

while True:
	print(f'\n{pc.room}')
	print(wrap(pc.room.description))
	args = input('Enter a cardinal direction or "h" for help: ')
	args = args.lower().split()
	try:
		act = args[0]
	except IndexError:
		print("It looks like you didn't enter anything parseable.")
		continue

	if len(args) > 1:
		obj = ' '.join(args[1:]).lower()
		if obj == 'it':
			try:
				obj = last
			except NameError:
				print('"it" is not supported when there has been no items specified yet.')
				continue

		if act in actions[get]:
			handle_get(pc.items, obj, pc.room)
		elif act in actions[drop]:
			handle_drop(pc.room.items, obj, pc)
		elif act in actions[attack]:
			handle_attack(pc, obj)
		elif act in actions[inspect]:
			handle_inspect(pc, obj)
		else:
			print(f'{act} is not a currently implemented action.')

		last = obj
		continue

	if act in commands[_quit]:
		print("\nYou've exited the game. Goodbye.")
		break
	if act in 'nswe':
		try:
			pc.move(act)
		except KeyError:
			print("The room doesn't seem to have an exit in that direction.")
	elif act in commands[inventory]:
		print(f'Inventory: {format_list(names(pc.items))}')
	elif act in commands[_help]:
		print(f'Possible commands: {format_list(flatten_object(commands))}')
		print(f'Possible actions: {format_list(flatten_object(actions))}')
	else:
		print("It looks like you didn't enter a cardinal direction.")

print()
