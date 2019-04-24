from data.rooms import rooms

class Character:
  def __init__(self, room, items = []):
    self.room = room
    self.items = items

  def move(self, roomName):
    self.room = rooms[roomName]
