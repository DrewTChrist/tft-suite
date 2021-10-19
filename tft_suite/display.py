import time

import digitalio
import board
import adafruit_rgb_display.st7789 as st7789
from PIL import Image, ImageDraw, ImageFont
from tft_suite.switcher import Switcher

class Display:
    """Display class representing an Adafruit Mini PiTFT"""

    def __init__(self, size, screens=None):

        # hardware
        self.display = None
        self.backlight = None
        self.buttonA = None
        self.buttonB = None

        # size
        self.width = None
        self.height = None

        # drawables
        self.image = None
        self.draw = None

        # screens
        self.screens = [] if not screens else screens

        self.initialize_hardware(size)
        self.initialize_drawables()

        self.switcher = Switcher(
            self.screens,
            **{
                'height': self.height,
                'width': self.width,
                'draw': self.draw,
                'image': self.image,
                'display': self.display
            }
        )

    def set_offsets(self, size):
        if size[0] == 135:
            self.display.x_offset = 53
            self.display.y_offset = 40
            #self.display.rotation = 90
        elif size[0] == 240:
            self.display.y_offset = 80
        #    self.display.rotation = 180


    def initialize_hardware(self, size):
        # Create the ST7789 display:
        self.display = st7789.ST7789(
            board.SPI(),
            cs=digitalio.DigitalInOut(board.CE0),
            dc=digitalio.DigitalInOut(board.D25),
            rst=None,
            baudrate=64000000,  # The pi can be very fast!
            width=size[0],
            height=size[1],
            x_offset=53,
            y_offset=40
        )
        self.backlight = digitalio.DigitalInOut(board.D22)
        self.backlight.switch_to_output()
        self.backlight.value = True

        self.buttonA = digitalio.DigitalInOut(board.D24)
        self.buttonB = digitalio.DigitalInOut(board.D23)

        self.buttonA.switch_to_input()
        self.buttonB.switch_to_input()

        self.set_offsets(size)

    def initialize_drawables(self):
        # flip these because the display is horizontal
        self.height = self.display.width
        self.width = self.display.height

        self.image = Image.new("RGB", (self.width, self.height))
        rotation = 90

        self.draw = ImageDraw.Draw(self.image)
        self.draw.rectangle((0, 0, self.width, self.height), outline=0, fill=(0,0,0))
        self.display.image(self.image, rotation)

    def enable_backlight(self):
        self.backlight.value = True
        
    def toggle_backlight(self):
        self.backlight.value = not self.backlight.value

    def start(self):
        while True:
            # A button is pushed
            if self.buttonA.value and not self.buttonB.value:
                self.switcher.switch_up()
                time.sleep(0.5)

            # B button is pushed
            if self.buttonB.value and not self.buttonA.value:
                self.switcher.switch_down()
                time.sleep(0.5)

            # Both buttons are pushed
            if not self.buttonA.value and not self.buttonB.value:
                self.toggle_backlight()
                time.sleep(0.5)

            self.switcher.create_thread()


