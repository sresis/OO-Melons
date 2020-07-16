############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name
        self.pairings = []

        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        # if list
        self.pairings.extend(pairing)

        #self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    muskmelon = MelonType('musk', 1998, 'green', True, True, "Muskmelon")
    muskmelon.add_pairing(['mint'])

    casaba = MelonType('cas', 2003, 'orange', False, False, "Casaba")
    casaba.add_pairing(['strawberries', 'mint'])
    
    crenshaw = MelonType('cren', 1996, 'green', False, False, "Crenshaw")
    crenshaw.add_pairing(['proscuitto'])

    yellow_watermelon = MelonType('yw', 2013, 'yellow', False, True, "Yellow Watermelon")
    yellow_watermelon.add_pairing(['ice cream'])

    all_melon_types.extend([muskmelon, casaba, crenshaw, yellow_watermelon])


    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print(f'{melon.name} pairs with:')
        for pairing in melon.pairings:
            print(f'- {pairing}')
        print()

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 



