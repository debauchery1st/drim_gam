import cocos
import pyglet

from DreamGame import DreamGame
from content.base_types.demo_hero import demohero_basetype
from content.dungeons.demo_dungeon import demo_dungeon
from game_objects.battlefield_objects.Unit import Unit
from gui.gameplay import GamePlayScene


class BackgroundMainMenuLayer(cocos.layer.ColorLayer):
    """STUB"""

    def __init__(self):
        __color = (255, 255, 255, 255)
        super(BackgroundMainMenuLayer, self).__init__(*__color)


class MenuMainMenuLayer(cocos.menu.Menu):
    """
        cocos.menu.Menu just inherits from cocos.layer.Layer so it's just a Layer
    """

    def __init__(self):
        super(MenuMainMenuLayer, self).__init__()

        self.menu_valign = cocos.menu.CENTER
        self.menu_halign = cocos.menu.CENTER

        self.font_item['color'] = (0, 0, 0, 255)
        self.font_item_selected['color'] = (192, 192, 192, 255)
        menu_items = [
            (cocos.menu.MenuItem("New game", self.new_game)),
            (cocos.menu.MenuItem("Load game", self.load_game)),
            (cocos.menu.MenuItem("Credits", self.show_credits)),
            (cocos.menu.MenuItem("Exit", self.on_quit()))
        ]

        self.create_menu(menu_items)

    def new_game(self):
        # TODO: we need switch scene to another here
        game = DreamGame.start_dungeon(demo_dungeon, Unit(demohero_basetype))
        print(game)
        game.print_all_units()
        game.player_berserk = True
        cocos.director.director.replace(GamePlayScene(game))
        # hero_turns = game.loop(player_berserk=True)
        # print("hero has made {} turns.".format(hero_turns))
        # self.on_exit()

    def load_game(self):
        pass

    def show_credits(self):
        pass

    def on_quit(self):
        # TODO: add some logic here
        pyglet.app.exit()


class MainMenuScene(cocos.scene.Scene):
    def __init__(self):
        super(MainMenuScene, self).__init__()

        self.add(
            BackgroundMainMenuLayer(), z=-1, name="background"
        )

        self.add(
            MenuMainMenuLayer(), z=0, name="main_layer"
        )
