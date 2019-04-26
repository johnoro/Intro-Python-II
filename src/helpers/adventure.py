from helpers.general import format_list_with_end, names, wrap
from helpers.items import find_similar

def printMultiple(found):
  print(wrap(
    f"I don't know which you mean: {format_list_with_end(names(found))}"
  ))


def transfer_item(itemName, src, handle_transfer):
  found = find_similar(src.items, itemName)

  if isinstance(found, list):
    length = len(found)
    if length == 0:
      found = None
    elif length == 1:
      found = found[0]
    else:
      printMultiple(found)
      return

  if found is not None:
    handle_transfer(found)
  else:
    print(f'{itemName.capitalize()} not found.')
