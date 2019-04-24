from characters.character import Character

class Monster(Character):
  def __init__(self, room, items = []):
    super().__init__(room, items)
