from data.characters import monsters

def get_monsters(room):
  roomsMons = []
  for name, monster in monsters.items():
    if monster.room is room:
      roomsMons.append(monster)
  return roomsMons
