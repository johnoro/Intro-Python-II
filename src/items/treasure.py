from items.item import Item
from helpers.items import remove_and_move

class Treasure(Item):
  def __init__(self, name, description, takeable = True, droppable = True, value = 0):
    super().__init__(name, description, takeable, droppable)
    self.value = value
  
  def on_take(self, room, player):
    if self.takeable:
      player.score += self.value
      self.value = 0
      remove_and_move(player.items, self, room)
      return True
    return False
