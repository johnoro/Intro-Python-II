outside = 'outside'
foyer = 'foyer'
overlook = 'overlook'
narrow = 'narrow'
treasure = 'treasure'

from data.items import quantum_microscope, intellicorium_microscope, splitting_microscope
from rooms.room import Room

# Declare all the rooms
rooms = {
	outside: Room(outside, 'Outside Cave Entrance',
								'North of you, the cave mount beckons.'),
	foyer: Room(foyer, 'Foyer', '''Dim light filters in from the south. Dusty
passages run north and east.'''),
	overlook: Room(overlook, 'Grand Overlook', '''A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.''', [quantum_microscope, intellicorium_microscope, splitting_microscope]),
	narrow: Room(narrow, 'Narrow Passage', '''The narrow passage bends here from west
to north. The smell of gold permeates the air.'''),
	treasure: Room(treasure, 'Treasure Chamber', '''You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.'''),
}

# Link rooms together
rooms[outside].set_dir('n', foyer)
rooms[foyer].set_dirs(dict(s=outside, n=overlook, e=narrow))
rooms[overlook].set_dir('w', foyer)
rooms[narrow].set_dirs(dict(w=foyer, n=treasure))
rooms[treasure].set_dir('s', narrow)
