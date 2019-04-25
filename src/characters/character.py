from data.rooms import rooms

class Character:
  def __init__(self, room, items = []):
    self.room = room
    self.items = items

  def move(self, direction):
    self.room = rooms[self.room.get_dir(direction)]
