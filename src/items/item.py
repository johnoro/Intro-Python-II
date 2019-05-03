from helpers.items import remove_and_move

class Item:
  def __init__(self, name, description, takeable = True, droppable = True):
    self.name = name
    self.description = description
    self.takeable = takeable
    self.droppable = droppable

  def on_take(self, room, player):
    if self.takeable:
      remove_and_move(player.items, self, room)
      return True
    return False

  def on_drop(self, player, room):
    if self.droppable:
      remove_and_move(room.items, self, player)
      return True
    return False
