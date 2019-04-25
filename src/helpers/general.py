import textwrap
def wrap(text, sep = '\n'):
  return sep.join(textwrap.wrap(text))

def names(objectsWithNames):
  return [o.name.lower() for o in objectsWithNames]

def format_list(l, sep = ', '):
  return sep.join(l)

def format_list_with_end(l, end = 'or'):
  last = l[-1]
  return f"{format_list(l[:-1])}{',' if len(l) > 2 else ''} {end} {last}"

from random import randint
def randBool():
  return randint(0, 1) == 0

def flatten_object(o):
  return [item for k, sl in o.items() for item in sl]
