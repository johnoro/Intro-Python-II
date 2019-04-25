from items.item import Item
from items.weapon import Weapon

quantum_microscope = Item('quantum microscope', 'A labelled microscope with odd inscriptions decorating its exterior.')
intellicorium_microscope = Item('intellicorium microscope', "A labelled microscope with so many inscriptions covering it that it's impossible to use.")
splitting_microscope = Item('splitting microscope', "A labelled microscope with a few inscriptions. Its view seems to split with eight different lenses, which doesn't lend well to its usage.")

pitchfork = Weapon(100, 'pitchfork', 'A stylish, devilish pitchfork with engravings covering its handle.', droppable=False)
