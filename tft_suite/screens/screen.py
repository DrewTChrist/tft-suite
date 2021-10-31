import abc
import subprocess
import threading
import time

import adafruit_rgb_display.st7789 as st7789
from PIL import Image, ImageDraw, ImageFont

class Screen(abc.ABC):
    
    def __init__(self, **kwargs) -> None:
       self.height: int = kwargs['height']
       self.width: int = kwargs['width']
       self.draw: ImageDraw.Draw = kwargs['draw']
       self.image: Image = kwargs['image']
       self.display: st7789.ST7789  = kwargs['display']
       self.font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)

    def run(self) -> None:
        t = threading.currentThread()
        while getattr(t, "do_run", True):
            try:
                self.draw_screen()
            except subprocess.CalledProcessError:
                t.do_run = False
                t.join()


    @abc.abstractmethod
    def draw_screen(self) -> None:
        pass

