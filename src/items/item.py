from helpers.items import remove_and_move

class Item:
  def __init__(self, name, description, takeable = True, droppable = True):
    self.name = name
    self.description = description
    self.takeable = takeable
    self.droppable = droppable

  def on_take(self, room, player_items):
    if self.takeable:
      remove_and_move(player_items, self, room)
      return True
    return False

  def on_drop(self, player, room_items):
    if self.droppable:
      remove_and_move(room_items, self, player)
      return True
    return False
