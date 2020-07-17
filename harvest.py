############
# Part 1   #
############

import re
import sys

textfile = open(sys.argv[1])

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

    melon_dict = {}
    for melon in melon_types:
        melon_dict[melon.code] = melon_dict.get(melon.code, melon)


    return melon_dict


############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    def __init__(self, code, shape_rating, color_rating, harvested_from, harvested_by):
        self.code = code
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.harvested_from = harvested_from
        self.harvested_by = harvested_by
        self.is_it_sellable = self.is_sellable()

    def is_sellable(self):
        return (self.shape_rating > 5 and self.color_rating > 5 and self.harvested_from != 3)


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    melons_by_id = make_melon_type_lookup(melon_types)

    all_melons = []

    melon_1 = Melon(melons_by_id['yw'], 8, 7, 2, 'Sheila')
    melon_2 = Melon(melons_by_id['yw'], 3, 4, 2, 'Sheila')
    melon_3 = Melon(melons_by_id['yw'], 9, 8, 3, 'Sheila')
    melon_4 = Melon(melons_by_id['cas'], 10, 6, 35, 'Sheila')
    melon_5 = Melon(melons_by_id['cren'], 8, 9, 35, 'Michael')
    melon_6 = Melon(melons_by_id['cren'], 8, 2, 35, 'Michael')
    melon_7 = Melon(melons_by_id['cren'], 2, 3, 4, 'Michael')
    melon_8 = Melon(melons_by_id['musk'], 6, 7, 4, 'Michael')
    melon_9 = Melon(melons_by_id['musk'], 7, 10, 3, 'Sheila')

    all_melons.extend([melon_1, melon_2, melon_3, melon_4, melon_5, melon_6, melon_7, melon_8, melon_9])

    return all_melons



def add_new_melons(textfile, melon_types):

    melon_log = open(textfile).read()

    melon_type = make_melon_type_lookup(melon_types)
  
    updated_list = []


    for line in melon_log.split("\n"):
        new_line = line.split(" ")
        shape = int(new_line[1])
        color = int(new_line[3])
        type_of_melon = str(new_line[5])
        harvested_by = str(new_line[8])
        field_num = int(new_line[11])
        new_melon = Melon(melon_type[type_of_melon], shape, color, field_num, harvested_by)
        updated_list.append(new_melon)
        
 

    return updated_list





#add_new_melons('harvest_log.txt', make_melon_types())



def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for single_melon in melons:
        if single_melon.is_sellable():
            print_output = '(CAN BE SOLD)'
        else:
            print_output = '(NOT SELLABLE)'
        print(f'Harvested by {single_melon.harvested_by} from field {single_melon.harvested_from} {print_output}')



get_sellability_report(add_new_melons('harvest_log.txt', make_melon_types()))






