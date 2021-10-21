import threading
import time
from typing import Tuple

from adafruit_rgb_display.rgb import color565
from tft_suite.screens.screen import Screen

class ColorScreen(Screen):
    
    def __init__(self, rgb: Tuple[int, int, int], **kwargs) -> None:
        super(ColorScreen, self).__init__(**kwargs)
        self.rgb: Tuple[int, int, int] = rgb

    def draw_screen(self) -> None:
        # Draw a black filled box to clear the image.
        self.draw.rectangle((0, 0, self.width, self.height), outline=0, fill=0)

        # Fill the screen with the current class rgb
        self.display.fill(color565(self.rgb[0], self.rgb[1], self.rgb[2]))



