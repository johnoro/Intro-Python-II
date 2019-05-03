from items.weapon import Weapon
from helpers.general import format_list_with_end, names, wrap, rand_bool
from helpers.items import find_similar
from helpers.adventure import print_multiple, transfer_item
from data.characters import pc
from data.characters import monsters

def handle_get(player, item_name, room):
  def get(found):
    nonlocal player, item_name, room
    item_name = item_name.capitalize()
    taken = found.on_take(room, player)
    if not taken:
      print(f'{item_name} cannot be taken.')
    else:
      print(f'{item_name} taken.')
  
  transfer_item(item_name, room, get)


def handle_drop(room, item_name, player):
  def drop(found):
    nonlocal room, item_name, player
    item_name = item_name.capitalize()
    dropped = found.on_drop(player, room)
    if not dropped:
      print(f'{item_name} cannot be dropped.')
    else:
      print(f'{item_name} dropped.')

  transfer_item(item_name, player, drop)


def handle_attack(attacker, attackee):
  if attackee is pc:
    print("You've taken some serious damage!")
    return

  for item in attacker.items:
    if isinstance(item, Weapon):
      # has_weapon = True
      break
  else:
    print('You have no weapons. How do you expect to attack anything?')
    return

  found = find_similar(monsters.values(), attackee)
  if isinstance(found, list):
    length = len(found)
    if length == 0:
      found = None
    elif length == 1:
      found = found[0]
    else:
      print_multiple(found)
      return

  attackee = attackee.capitalize()
  if found is not None:
    attacked = found.take_damage(attacker.damage)
    if not attacked:
      print(f'{attackee} could not be attacked.')
    else:
      if rand_bool():
        attacker.take_damage(found.damage)
        print(f'{attackee} fought back!')
  else:
    print(f'{attackee} not found.')


# add damage for weapons
def handle_inspect(player, item_name):
  items = player.room.items + player.items
  
  found = find_similar(items, item_name)
  if isinstance(found, list):
    length = len(found)
    if length == 0:
      found = None
    elif length == 1:
      found = found[0]
    else:
      print_multiple(found)
      return
  
  item_name = item_name.capitalize()
  if found is not None:
    print(wrap(f'{item_name}: {found.description}'))
  else:
    print(f'{item_name} not found.')
