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

def move(items, item, name):
  if item is None:
    print(f'{name} was not found.')
  else:
    items.append(item)

def removeAndMove(items, item, srcObj):
  removed = srcObj.removeItem(item.name)
  items.append(removed)
