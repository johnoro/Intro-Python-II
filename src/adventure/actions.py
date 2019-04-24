from helpers.items import find

def transferItem(items, itemName, src, handleTransfer):
  found = find(src.items, itemName)

  if found is not None:
    handleTransfer(found)
  else:
    print(f'{itemName} not found.')


def handleGet(playerItems, itemName, room):
  def handleTake(found):
    nonlocal playerItems, itemName, room
    itemName = itemName.capitalize()
    taken = found.onTake(room, playerItems)
    if not taken:
      print(f'{itemName} cannot be taken.')
    else:
      print(f'{itemName} taken.')
  
  transferItem(playerItems, itemName, room, handleTake)


def handleDrop(roomItems, itemName, player):
  def handleDrop(found):
    nonlocal roomItems, itemName, player
    itemName = itemName.capitalize()
    dropped = found.onDrop(player, roomItems)
    if not dropped:
      print(f'{itemName} cannot be dropped.')
    else:
      print(f'{itemName} dropped.')

  transferItem(roomItems, itemName, player, handleDrop)
