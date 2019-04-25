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

def find_by_base_name(items, name):
  found = [find(items, name)]
  if found[0] is not None:
    return found
  
  found.pop()
  for i in items:
    if i.name.split()[-1] == name:
      found.append(i)
  return found
