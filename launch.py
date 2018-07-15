import cocos
from gui.base import init_gui
from gui.menu import MainMenuScene

init_gui()

main_menu_scene = MainMenuScene()
cocos.director.director.run(main_menu_scene)
