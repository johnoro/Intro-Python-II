from characters.character import Character

# Write a class to hold player information, e.g. what room they are in
# currently.
class Player(Character):
  def __init__(self, room, items = []):
    super().__init__(room, items)
