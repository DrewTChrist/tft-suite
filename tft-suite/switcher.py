import threading
import time

class Switcher:

    def __init__(self, screens):
        self.screens = screens
        self.index = 0
        self.screenthread = threading.Thread(target=lambda: screens[screen_idx](height, width, draw, image, display))
        screenthread.start()

        # Main loop:
        while True:

            if buttonA.value and not buttonB.value:
                if abs(screen_idx - 1) < len(screens):
                    screen_idx = screen_idx - 1
                else:
                    screen_idx = 0
                screenthread.do_run = False
                screenthread.join()
                time.sleep(0.5)

            if buttonB.value and not buttonA.value:
                if abs(screen_idx + 1) < len(screens):
                    screen_idx = screen_idx + 1
                else:
                    screen_idx = 0
                screenthread.do_run = False
                screenthread.join()
                time.sleep(0.5)

            if not buttonA.value and not buttonB.value:
                backlight.value = not backlight.value
                time.sleep(0.5)

            if not screenthread.is_alive():
                screenthread = threading.Thread(target=lambda: screens[screen_idx](height, width, draw, image, display))
                screenthread.do_run = True
                screenthread.start()


