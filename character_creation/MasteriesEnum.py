from utils.named_enums import NameEnum, auto
from functools import lru_cache
from common import xprint


class MasteriesEnum(NameEnum):
    AXE = auto()
    SWORD = auto()
    DAGGER = auto()
    SPEAR = auto()
    CLUB = auto()
    HAMMER = auto()
    EXOTIC = auto()
    SHIELD = auto()
    DUAL = auto()
    TWO_HANDED = auto()

    FIRE = auto()
    FROST  = auto()
    LIGHTNING  = auto()
    EARTH = auto()
    ACID  = auto()
    LIGHT  = auto()
    SONIC  = auto()
    ASTRAL = auto()
    MIND = auto()

    RANGED = auto()
    THROW = auto()
    STEALTH = auto()
    SEARCH = auto()
    MONSTROLOGY = auto()
    ACROBATICS = auto()
    ATHLETICS = auto()
    ARMORY = auto()
    LORE = auto()
    ALCHEMY = auto()

class MasteriesGroups:

    m = MasteriesEnum
    sporty = [m.ATHLETICS, m.TWO_HANDED, m.DUAL, m.SHIELD]
    chop_chop_chop = [m.AXE, m.HAMMER, m.TWO_HANDED, m.SWORD]
    stabby = [m.DAGGER, m.SPEAR, m.EXOTIC]
    bashy = [m.CLUB, m.HAMMER, m.SHIELD]
    assasin = [m.DAGGER, m.DUAL, m.ACROBATICS, m.STEALTH, m.SEARCH]
    sniping = [m.RANGED, m.THROW, m.LIGHT, m.SPEAR, m.SEARCH]
    spicky = [m.SPEAR, m.LIGHTNING, m.LIGHT]
    loud = [m.SONIC, m.HAMMER, m.TWO_HANDED, m.EARTH]
    explosive = [m.FIRE, m.EARTH, m.SONIC, m.AXE]
    cold = [m.ARMORY, m.SWORD, m.DAGGER, m.FROST]
    arcane = [m.MIND, m.ASTRAL, m.LORE, m.MONSTROLOGY, m.ALCHEMY]
    chemical = [m.ACID, m.ALCHEMY, m.EARTH, m.MONSTROLOGY]
    defensive = [m.SHIELD, m.ARMORY, m.EARTH]
    all_battle = [m.CLUB, m.SWORD, m.AXE, m.ARMORY, m.DAGGER, m.SPEAR,
                  m.RANGED, m.EXOTIC, m.HAMMER, m.SHIELD, m.DUAL, m.TWO_HANDED]

    all_magic = [m.FROST, m.FIRE, m.LIGHT, m.LIGHTNING, m.EARTH,
                 m.ACID, m.SONIC, m.ASTRAL, m.MIND]

    all_misc = [m.THROW, m.STEALTH, m.SEARCH, m.MONSTROLOGY, m.ACROBATICS, m.ATHLETICS,
                m.LORE, m.ALCHEMY]

    all = [sporty, chop_chop_chop, stabby, bashy,
           assasin, sniping, spicky, loud, cold,
           arcane, chemical, defensive, explosive, all_battle, all_magic, all_misc]

    coupling_coef = 0.5

    @classmethod
    @lru_cache()
    def occurances(cls, m):
        n = 0
        for lst in cls.all:
            for member in lst:
                if member is m:
                    n += 1

        return n


    @classmethod
    @lru_cache()
    def total_occurances(cls):
        result = 0
        for m in MasteriesEnum:
            result += cls.occurances(m)

        return result


    @classmethod
    @lru_cache(maxsize=2048)
    def coupling(cls, m1, m2):
        coupling = 0
        for group in cls.all:
            if m1 in group and m2 in group:
                coupling += 1

        return coupling * cls.coupling_coef / ( 1 + cls.occurances(m1) + cls.occurances(m2))


if __name__ == "__main__":
    for m in MasteriesEnum:
        xprint(m, MasteriesGroups.occurances(m))
    xprint(MasteriesGroups.total_occurances())

    for m1 in MasteriesEnum:
        for m2 in MasteriesEnum:
            xprint(m1, m2, MasteriesGroups.coupling(m1, m2))
