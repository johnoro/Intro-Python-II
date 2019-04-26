from helpers.general import format_list, names
from helpers.rooms import new_directions

class Room:
  def __init__(self, key, name, description, items = [], dirs = {}):
    self.key = key
    self.name = name
    self.description = description
    self.items = items
    self.dirs = new_directions(dirs)

  def __str__(self):
    dirs = [d for d in self.dirs if self.dirs[d] is not None]
    dirs = f'\nAvailable directions: {format_list(dirs)}'
    items = names(self.items)
    items = f'\nItems: {format_list(items)}' if len(items) > 0 else ''
    return self.name + items + dirs + self.get_mons()

  def get_dir(self, direction):
    return self.dirs[direction]

  def set_dir(self, direction, room):
    self.dirs[direction] = room

  def set_dirs(self, dirs):
    self.dirs = new_directions(dirs)

  def get_mons(self):
    from helpers.characters import get_monsters
    mons = names(get_monsters(self))
    mons = f'\nMonsters: {format_list(mons)}' if len(mons) > 0 else ''
    return mons
