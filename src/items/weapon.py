from items.item import Item

class Weapon(Item):
  def __init__(self, name, description, damage, \
              takeable = True, droppable = True):
    super().__init__(name, description)
    self.damage = damage
