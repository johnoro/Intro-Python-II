def names(items):
  return [i.name.lower() for i in items]

def find(items, name):
  for i in items:
    if i.name == name:
      return i
  return None

def remove(items, name):
  found = find(items, name)
  if found is not None:
    items.remove(found)
  return found

def remove_and_move(items, item, src_obj):
  removed = remove(src_obj.items, item.name)
  items.append(removed)
