import cocos
from gui.base import init_gui, load_resources
from gui.menu import MainMenuScene

init_gui()
load_resources()

main_menu_scene = MainMenuScene()
cocos.director.director.run(main_menu_scene)
