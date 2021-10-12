import digitalio
import board
import adafruit_rgb_display.st7789 as st7789
from PIL import Image, ImageDraw, ImageFont
from screens import screens
from switcher import Switcher

class Display:

    def __init__(self):

        self.display = None
        self.backlight = None
        self.buttonA = None
        self.buttonB = None
        self.height = None
        self.width = None
        self.image = None
        self.draw = None
        self.screens = []

        self.initialize_hardware()
        self.initialize_drawables()
        self.initialize_screens()

        self.switcher = Switcher(self.screens)

    def initalize_hardware(self):
        # Create the ST7789 display:
        self.display = st7789.ST7789(
            board.SPI(),
            cs=digitalio.DigitalInOut(board.CE0),
            dc=digitalio.DigitalInOut(board.D25),
            rst=None,
            baudrate=64000000,  # The pi can be very fast!
            width=135,
            height=240,
            x_offset=53,
            y_offset=40,
        )
        self.backlight = digitalio.DigitalInOut(board.D22)
        self.backlight.switch_to_output()
        self.backlight.value = True

        self.buttonA = digitalio.DigitalInOut(board.D23)
        self.buttonB = digitalio.DigitalInOut(board.D24)

        self.buttonA.switch_to_input()
        self.buttonB.switch_to_input()

    def initialize_drawables(self):
        # flip these because the display is horizontal
        self.height = display.width
        self.width = display.height

        self.image = Image.new("RGB", (self.width, self.height))
        rotation = 90

        self.draw = ImageDraw.Draw(self.image)
        self.draw.rectangle((0, 0, self.width, self.height), outline=0, fill=(0,0,0))
        self.display.image(self.image, rotation)

        self.font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)

    def initalize_screens(self):
        self.screens = [
            screens.fill_red, 
            screens.fill_green, 
            screens.fill_blue, 
            screens.stats, 
            screens.networks
        ]
        
    def toggle_backlight(self):
        self.backlight.value = not self.backlight.value
