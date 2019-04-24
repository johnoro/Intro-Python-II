from helpers.general import formatList
from helpers.items import names

# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
  def __init__(self, key, name, description, items = []):
    self.key = key
    self.name = name
    self.description = description
    self.items = items
    self.dirs = {'n': None, 's': None, 'w': None, 'e': None}

  def __str__(self):
    dirs = [ d for d in self.dirs if self.dirs[d] is not None ]
    dirs = f"\nAvailable directions: {formatList(dirs)}"
    items = names(self.items)
    items = f"\nItems: {formatList(items)}" if len(items) > 0 else ''
    return self.name + items + dirs

  def getDir(self, direction):
    return self.dirs[direction]

  def setDir(self, direction, room):
    self.dirs[direction] = room
