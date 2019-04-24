from helpers.items import remove

# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
  def __init__(self, room, items = []):
    self.room = room
    self.items = items

  def removeItem(self, itemName):
    return remove(self.items, itemName)
