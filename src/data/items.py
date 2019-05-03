from items.treasure import Treasure
from items.weapon import Weapon

quantum_microscope = Treasure('quantum microscope', 'A labelled microscope with odd inscriptions decorating its exterior.', value=100)
intellicorium_microscope = Treasure('intellicorium microscope', "A labelled microscope with so many inscriptions covering it that it's impossible to use.", value=75)
splitting_microscope = Treasure('splitting microscope', "A labelled microscope with a few inscriptions. Its view seems to split with eight different lenses, which doesn't lend well to its usage.", value=50)

pitchfork = Weapon('pitchfork', 'A stylish, devilish pitchfork with engravings covering its handle.', damage=100, droppable=False)
sword = Weapon('sword', 'A plain old sword.', damage=50)
