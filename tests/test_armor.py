from mechanics.damage import Armor, DamageTypes, deal_damage, Damage
import pytest


def test_armor_only_vs_valid_damage_types():
    armor = Armor(3)
    with pytest.raises(AssertionError):
        armor["BULLSHIT_DAMAGE_TYPE"] = 55

def test_armor_reduces_damage(hero):

    hp_before_dmg = hero.health
    dmg = Damage(5, DamageTypes.FIRE)
    deal_damage(dmg, hero)

    dealt_no_armor = hp_before_dmg - hero.health
    hp_before_dmg = hero.health


    armor = Armor(3)
    hero.armor = armor

    deal_damage(dmg, hero)
    dealt_armor = hp_before_dmg - hero.health

    assert dealt_no_armor > dealt_armor


@pytest.fixture(params=DamageTypes)
def dmg(request):
    yield Damage(5, request.param)

def test_types_matter(hero, dmg):

    hp_before_dmg = hero.health

    armor = Armor(3, {DamageTypes.FIRE: 4000})
    hero.armor = armor

    deal_damage(dmg, hero)

    if dmg.type == DamageTypes.FIRE:
        assert hp_before_dmg == hero.health
    else:
        assert hp_before_dmg > hero.health

