import subprocess
import threading
import time

from tft_suite.screens.screen import Screen
from tft_suite.cmd_parser import iwlist_parser

class NetworksScreen(Screen):

    def __init__(self, **kwargs):
        super(NetworksScreen, self).__init__(**kwargs)

    def draw_screen(self):
        rotation = 90
        y = 0

        # Draw a black filled box to clear the image.
        self.draw.rectangle((0, 0, self.width, self.height), outline=0, fill=0)

        # Shell scripts for system monitoring from here:
        # https://unix.stackexchange.com/questions/119126/command-to-display-memory-usage-disk-usage-and-cpu-load
        #cmd = 'iwlist wlan0 scan | grep "ESSID:"'
        #sudo iwlist wlan0 scan | awk -F ':' '/ESSID:/ {if ($2 != "\"\""){print $2;}}'
        #cmd = r"""sudo iwlist wlan0 scan | awk -F ':' '/ESSID:/ {if ($2 != "\"\""){print $2;}}'"""
        cmd = 'iwlist wlan0 scan'
        nets = subprocess.check_output(cmd, shell=True).decode("utf-8")
        nets = '\n'.join([f"{x['ESSID']} - Key:{x['Encryption key']}" for x in iwlist_parser(nets)])

        # Write four lines of text.
        #draw.text((x, y), nets, font=font, fill="#FFFFFF")
        self.draw.text((0, y), nets, font=self.font, fill="#FFFFFF")

        y -= 10

        # Display image.
        self.display.image(self.image, rotation)
        time.sleep(0.1)
