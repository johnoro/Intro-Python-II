from data.rooms import rooms

class Character:
  def __init__(self, room, items = []):
    self.room = room
    self.items = items
    self.health = 100

  def move(self, direction):
    self.room = rooms[self.room.get_dir(direction)]

  def take_damage(self, damage = 100):
    # checks defense; if defense greater than damage, return False
    # checks health
    # sustains damage or dies
    return True
