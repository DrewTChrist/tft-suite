import threading
import time
import digitalio
import board

from PIL import Image, ImageDraw, ImageFont
from adafruit_rgb_display.rgb import color565
import adafruit_rgb_display.st7789 as st7789

import screens

# Configuration for CS and DC pins for Raspberry Pi
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None
BAUDRATE = 64000000  # The pi can be very fast!

# Create the ST7789 display:
display = st7789.ST7789(
    board.SPI(),
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)

backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

height = display.width
width = display.height
image = Image.new("RGB", (width, height))
rotation = 90

draw = ImageDraw.Draw(image)
draw.rectangle((0, 0, width, height), outline=0, fill=(0,0,0))
display.image(image, rotation)

padding = -2
top = padding
bottom = height - padding
x = 0

font = ImageFont.truetype("usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)

colors = [color565(255, 0, 0),color565(0, 0, 255),color565(0, 255, 0)]

def fill_red(height, width, draw, image, display):
    t = threading.currentThread()
    while getattr(t, "do_run", True):
        display.fill(colors[0])

def fill_blue(height, width, draw, image, display):
    t = threading.currentThread()
    while getattr(t, "do_run", True):
        display.fill(colors[1])

def fill_green(height, width, draw, image, display):
    t = threading.currentThread()
    while getattr(t, "do_run", True):
        display.fill(colors[2])

screens = [fill_red, fill_green, fill_blue, screens.stats, screens.networks]
idx = 0

screenthread = threading.Thread(target=lambda: screens[idx](height, width, draw, image, display))
screenthread.start()

# Main loop:
while True:

    if buttonA.value and not buttonB.value:
        if abs(idx - 1) < len(screens):
            idx = idx - 1
        else:
            idx = 0
        screenthread.do_run = False
        screenthread.join()
        time.sleep(0.5)

    if buttonB.value and not buttonA.value:
        if abs(idx + 1) < len(screens):
            idx = idx + 1
        else:
            idx = 0
        screenthread.do_run = False
        screenthread.join()
        time.sleep(0.5)

    if not buttonA.value and not buttonB.value:
        backlight.value = not backlight.value
        time.sleep(0.5)

    if not screenthread.is_alive():
        screenthread = threading.Thread(target=lambda: screens[idx](height, width, draw, image, display))
        screenthread.do_run = True
        screenthread.start()


