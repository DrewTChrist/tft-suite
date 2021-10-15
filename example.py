from tft_suite.display import Display
from tft_suite.screens.stats_screen import StatsScreen
from tft_suite.screens.networks_screen import NetworksScreen
from tft_suite.screens.color_screen import ColorScreen
from tft_suite.screens.image_screen import ImageScreen

if __name__ == '__main__':
    Display([
        (StatsScreen, ()),
        (NetworksScreen, ()),
        (ColorScreen, ((255, 0, 0),)),
        (ColorScreen, ((0, 255, 0),)),
        (ColorScreen, ((0, 0, 255),)),
        (ImageScreen, (('/home/pi/python/python.jpg'),))
    ]).start()
