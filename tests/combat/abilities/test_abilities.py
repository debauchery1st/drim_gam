import pytest

from game_objects.attributes import Bonus, Attribute
from game_objects.battlefield_objects import CharAttributes, get_attrib_by_enum
from mechanics.buffs import Ability


@pytest.fixture(params=CharAttributes)
def attrib(request):
    yield request.param

@pytest.fixture()
def inner_power(attrib):
    bonus = Attribute(2, 100, 0)
    inner_power_bonus = Bonus({attrib: bonus})
    inner_power = Ability([inner_power_bonus])

    yield inner_power

@pytest.fixture()
def bonus_str():
    bonus = Attribute(0, 0, 50)
    bonus_hp = Bonus({CharAttributes.HEALTH: bonus})
    abil_hp = Ability([bonus_hp])

    yield abil_hp



def test_str_helps(hero, inner_power, attrib):

    attrib_before = get_attrib_by_enum(hero, attrib)

    inner_power.apply_to(hero)
    hero.reset()

    attrib_after = get_attrib_by_enum(hero, attrib)

    assert attrib_after > attrib_before

def test_rescale(hero, bonus_str):
    hp_before = hero.health

    bonus_str.apply_to(hero)
    hp_after = hero.health

    assert hp_after > hp_before

def test_multiplier(hero, pirate):

    bonus = Attribute(0, 50, 0)
    bonus_hp = Bonus({CharAttributes.HEALTH: bonus})
    abil_hp = Ability([bonus_hp])

    hp_before = hero.health
    abil_hp.apply_to(hero)
    delta_hero = hero.health - hp_before

    hp_before = pirate.health
    abil_hp.apply_to(pirate)
    delta_pirate = pirate.health - hp_before

    assert delta_hero > delta_pirate

def test_bonus(hero, pirate):

    bonus = Attribute(0, 0, 50)
    bonus_hp = Bonus({CharAttributes.HEALTH: bonus})
    abil_hp = Ability([bonus_hp])

    hp_before = hero.health
    abil_hp.apply_to(hero)

    delta_hero = hero.health - hp_before

    assert delta_hero > 0

    hp_before = pirate.health
    abil_hp.apply_to(pirate)
    delta_pirate = pirate.health - hp_before

    assert delta_hero == delta_pirate


