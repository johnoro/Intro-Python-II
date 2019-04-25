from helpers.items import find

def transfer_item(items, itemName, src, handle_transfer):
  found = find(src.items, itemName)

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
  
  transfer_item(player_items, item_name, room, get)


def handle_drop(room_items, item_name, player):
  def drop(found):
    nonlocal room_items, item_name, player
    item_name = item_name.capitalize()
    dropped = found.on_drop(player, room_items)
    if not dropped:
      print(f'{item_name} cannot be dropped.')
    else:
      print(f'{item_name} dropped.')

  transfer_item(room_items, item_name, player, drop)
