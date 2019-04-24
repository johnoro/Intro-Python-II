from helpers.items import removeAndMove

class Item:
  def __init__(self, name, description, takeable = True, droppable = True):
    self.name = name
    self.description = description
    self.takeable = takeable
    self.droppable = droppable

  def onTake(self, room, playerItems):
    if self.takeable:
      removeAndMove(playerItems, self, room)
      return True
    return False

  def onDrop(self, player, roomItems):
    if self.droppable:
      removeAndMove(roomItems, self, player)
      return True
    return False
