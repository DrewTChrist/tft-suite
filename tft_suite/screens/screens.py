from adafruit_rgb_display.rgb import color565

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

