from tft_suite.display import Display
from tft_suite.screens.stats_screen import StatsScreen
from tft_suite.screens.networks_screen import NetworksScreen
from tft_suite.screens.red_screen import RedScreen

if __name__ == '__main__':
    Display([
        StatsScreen,
        NetworksScreen,
        RedScreen
    ]).start()
