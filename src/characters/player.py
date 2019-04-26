from characters.character import Character

class Player(Character):
  def __init__(self, room, items = []):
    super().__init__(room, items)
