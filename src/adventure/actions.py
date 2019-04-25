from items.weapon import Weapon
from helpers.general import format_list_with_end, names, wrap
from helpers.items import find_similar
from data.characters import pc
from data.characters import monsters

def printMultiple(found):
  print(wrap(
    f"I don't know which you mean: {format_list_with_end(names(found))}"
  ))


def transfer_item(itemName, src, handle_transfer):
  found = find_similar(src.items, itemName)

  if isinstance(found, list):
    length = len(found)
    if length == 0:
      found = None
    elif length == 1:
      found = found[0]
    else:
      printMultiple(found)
      return

  if found is not None:
    handle_transfer(found)
  else:
    print(f'{itemName.capitalize()} not found.')


def handle_get(player_items, item_name, room):
  def get(found):
    nonlocal player_items, item_name, room
    item_name = item_name.capitalize()
    taken = found.on_take(room, player_items)
    if not taken:
      print(f'{item_name} cannot be taken.')
    else:
      print(f'{item_name} taken.')
  
  transfer_item(item_name, room, get)


def handle_drop(room_items, item_name, player):
  def drop(found):
    nonlocal room_items, item_name, player
    item_name = item_name.capitalize()
    dropped = found.on_drop(player, room_items)
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
      printMultiple(found)
      return

  attackee = attackee.capitalize()
  if found is not None:
    attacked = found.take_damage(attacker.damage)
    if not attacked:
      print(f'{attackee} could not be attacked.')
  else:
    print(f'{attackee} not found.')


def handle_inspect(player, itemName):
  items = player.room.items + player.items
  
  found = find_similar(items, itemName)
  if isinstance(found, list):
    length = len(found)
    if length == 0:
      found = None
    elif length == 1:
      found = found[0]
    else:
      printMultiple(found)
      return
  
  itemName = itemName.capitalize()
  if found is not None:
    print(wrap(f'{itemName}: {found.description}'))
  else:
    print(f'{itemName} not found.')
