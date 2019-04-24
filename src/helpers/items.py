def names(items):
  return [i.name.lower() for i in items]

def remove(items, name):
  for i in items:
    if i.name == name:
      items.remove(i)
      return i
  return None

def move(items, item, obj):
  if item is None:
    print(f'{obj} was not found.')
  else:
    items.append(item)
