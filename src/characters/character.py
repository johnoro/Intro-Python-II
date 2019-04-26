from data.rooms import rooms

class Character:
  def __init__(self, room, items = []):
    self.room = room
    self.items = items
    self.health = 100
    self.damage = 50
    self.defense = 25

  def move(self, direction):
    self.room = rooms[self.room.get_dir(direction)]

  def take_damage(self, damage = 100):
    damage -= self.defense
    if damage <= 0:
      print('Defense is higher than or equal to damage.')
      return False
    self.health -= damage
    print(f'Damage taken: {damage}, current health: {self.health}')
    if self.health <= 0:
      print("It looks like death should've occurred here...")
      print("Time to break the rules of death and restore some health.")
      self.health = 75
    return True
