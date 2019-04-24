from helpers.items import removeAndMove

class Item:
  def __init__(self, name, description):
    self.name = name
    self.description = description

  def onTake(self, room, playerItems):
    removeAndMove(playerItems, self, room)

  def onDrop(self, player, roomItems):
    removeAndMove(roomItems, self, player)
