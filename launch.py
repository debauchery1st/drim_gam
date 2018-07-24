from DreamGame import DreamGame
from content.base_types.demo_hero import demohero_basetype
from content.dungeons.demo_dungeon import demo_dungeon
from game_objects.battlefield_objects.Unit import Unit

from common import xprint


def demo_game():
    game = DreamGame.start_dungeon(demo_dungeon(), Unit(demohero_basetype))
    return game


def demo_dream():
    game = demo_game()
    xprint(game)
    game.print_all_units()
    hero_turns = game.loop(player_berserk=True)
    xprint("hero has made {} turns.".format(hero_turns))


if __name__ == "__main__":
    demo_dream()
