from tft_suite.screens.screen import Screen
import threading
import time

from adafruit_rgb_display.rgb import color565

class RedScreen(Screen):
    
    def __init__(self, **kwargs):
        super(RedScreen, self).__init__(**kwargs)

    def run(self):
        t = threading.currentThread()
        rotation = 90
        padding = -2
        top = padding
        bottom = self.height - padding
        x = 0

        while getattr(t, "do_run", True):
            # Draw a black filled box to clear the image.
            self.draw.rectangle((0, 0, self.width, self.height), outline=0, fill=0)
            self.display.fill(color565(255, 0, 0))



