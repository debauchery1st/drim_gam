import cocos
import pyglet
from cfg import CFG


def init_gui():
    cocos.director.director.init(
        width=CFG.screen_width, height=CFG.screen_height,
        caption="Dream Game", fullscreen=False,
        do_not_scale=True  # https://stackoverflow.com/questions/16945039/issue-with-displaying-sprites-in-cocos2d
    )


def load_resources():
    pyglet.resource.path = ['resources', 'resources/icons', 'resources/icons/unit', 'resources/tiles']
    pyglet.resource.reindex()
