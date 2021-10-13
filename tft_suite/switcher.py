import threading
import time

class Switcher:

    def __init__(self, screens, **kwargs):
        self.screens = screens
        self.index = 0
        self.display = kwargs
        self.screenthread = threading.Thread(target=lambda: self.screens[self.index](**kwargs).run())

    def start(self):
        self.screenthread.start()

    def create_thread(self):
        if not self.screenthread.is_alive():
            self.screenthread = threading.Thread(target=lambda: self.screens[self.index](**kwargs).run())
            self.screenthread.do_run = True
            self.screenthread.start()

    def switch_up(self):
        if abs(self.index - 1) < len(self.screens):
            self.index = self.index - 1
        else:
            self.index = 0
        self.screenthread.do_run = False
        self.screenthread.join()

    def switch_down(self):
        if abs(self.index + 1) < len(self.screens):
            self.index = self.index + 1
        else:
            self.index = 0
        self.screenthread.do_run = False
        self.screenthread.join()

