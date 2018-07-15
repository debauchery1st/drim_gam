import cocos
from cfg import CFG


def init_gui():
    cocos.director.director.init(
        width=CFG.screen_width, height=CFG.screen_height,
        caption="Dream Game", fullscreen=False
    )
