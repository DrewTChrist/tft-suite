from tft_suite.display import Display
from tft_suite.screens.stats_screen import StatsScreen

if __name__ == '__main__':
    d = Display([StatsScreen])
    d.start()
