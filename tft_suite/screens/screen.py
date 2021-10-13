import abc
import subprocess
import threading
import time

from PIL import ImageFont

class Screen(abc.ABC):
    
    def __init__(self, **kwargs):
       self.height = height
       self.width = width
       self.draw = draw
       self.image = image
       self.display = display
       self.font = ImageFont.truetype("usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)

    @abc.abstractmethod
    def run(self):
        pass
