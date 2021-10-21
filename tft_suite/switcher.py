import threading
import time

class Switcher:
    """ This class is responsible for switching between screens and managing
        threads for those screens.
    """

    def __init__(self, screens, **kwargs):
        self.screens = screens
        self.target = lambda: self.screens[self.index][0](*self.screens[self.index][1], **self.args).run()
        self.index = 0
        self.args = kwargs
        self.screenthread = threading.Thread(target=self.target)
        self.running = False

    def start(self):
        if not self.screenthread.is_alive():
            self.running = True
            self.screenthread = threading.Thread(target=self.target)
            self.screenthread.do_run = True
            self.screenthread.start()

    def stop(self):
        self.running = False
        self.screenthread.do_run = False
        self.screenthread.join()

    def create_thread(self):
        if not self.screenthread.is_alive() and self.running:
            self.screenthread = threading.Thread(target=self.target)
            self.screenthread.do_run = True
            self.screenthread.start()

    def switch_up(self):
        self.stop()
        if abs(self.index - 1) < len(self.screens):
            self.index = self.index - 1
        else:
            self.index = 0
        self.start()

    def switch_down(self):
        self.stop()
        if abs(self.index + 1) < len(self.screens):
            self.index = self.index + 1
        else:
            self.index = 0
        self.start()

