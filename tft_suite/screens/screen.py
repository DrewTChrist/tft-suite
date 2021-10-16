import abc
import subprocess
import threading
import time

from PIL import ImageFont

class Screen(abc.ABC):
    
    def __init__(self, **kwargs):
       self.height = kwargs['height']
       self.width = kwargs['width']
       self.draw = kwargs['draw']
       self.image = kwargs['image']
       self.display = kwargs['display']
       self.font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)

    def run(self):
        t = threading.currentThread()
        while getattr(t, "do_run", True):
            self.draw_screen()

    @abc.abstractmethod
    def draw_screen(self):
        pass

