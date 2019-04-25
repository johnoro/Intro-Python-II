from characters.player import Player
from characters.monster import Monster
from data.rooms import rooms, outside, treasure
from data.items import pitchfork

# Make a new player object that is currently in the 'outside' room.
pc = Player(rooms[outside])

rabble_rouser = 'rabble rouser'
monsters = {
  rabble_rouser: Monster(rabble_rouser, rooms[treasure], [pitchfork])
}
