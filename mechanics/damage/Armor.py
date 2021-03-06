from mechanics.damage.DamageTypes import DamageTypes
from collections import UserDict

class Armor(UserDict):
    MIN_ARMOR = 0

    def __init__(self, base_value = 0, armor_dict=None):
        super().__init__()
        for dtype in DamageTypes:
            self[dtype] = base_value
        if armor_dict:
            self.update(armor_dict)


    def __setitem__(self, key, value):
        assert isinstance(key, DamageTypes)
        if value < Armor.MIN_ARMOR:
            super().__setitem__(key, Armor.MIN_ARMOR)
        else:
            super().__setitem__(key, int(value) )

    def __add__(self, other):
        result = {}
        for damage_type in self.keys():
            result[damage_type] = self[damage_type] + other[damage_type]
        return Armor(armor_dict=result)

    def __mul__(self, other):
        assert other < 1e20 # is a number

        result = {}
        for damage_type in self.keys():
            result[damage_type] = self[damage_type] * other
        return Armor(armor_dict=result)

