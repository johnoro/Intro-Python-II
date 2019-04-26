from characters.player import Player
from characters.monster import Monster
from data.rooms import rooms, outside, treasure
from data.items import pitchfork

pc = Player(rooms[outside])

rabble_rouser = 'rabble rouser'
monsters = {
  rabble_rouser: Monster(rabble_rouser, rooms[treasure], [pitchfork])
}
