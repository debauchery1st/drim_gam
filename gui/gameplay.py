import cocos
import pyglet


class BackgroundGamePlayLayer(cocos.layer.ColorLayer):
    """STUB"""

    def __init__(self):
        __color = (0, 0, 0, 255)
        super(BackgroundGamePlayLayer, self).__init__(*__color)


class MapLayer(cocos.layer.ScrollableLayer):
    def __init__(self, battlefield):
        super(MapLayer, self).__init__()
        for x in range(battlefield.w):
            for y in range(battlefield.h):
                grass_image = pyglet.resource.image('cell.png')
                cell_sprite = cocos.sprite.Sprite(grass_image,
                                                  (x * 32, y * 32))
                self.add(cell_sprite)


class GamePlayScene(cocos.scene.Scene):
    def __init__(self, instance):
        super(GamePlayScene, self).__init__()
        self.instance = instance
        map_layer = MapLayer(instance.battlefield)

        self.scrolling_manager = cocos.layer.ScrollingManager()
        self.scrolling_manager.add(map_layer)
        self.scrolling_manager.set_focus(  # temporary
            cocos.director.director._window_virtual_width / 2, cocos.director.director._window_virtual_height / 2
        )

        self.add(
            BackgroundGamePlayLayer(), z=-1, name='background'
        )

        self.add(self.scrolling_manager, z=0, name='battlefield')
