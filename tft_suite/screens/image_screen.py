from tft_suite.screens.screen import Screen
import threading
import time

from PIL import Image


class ImageScreen(Screen):

    def __init__(self, img_path: str, **kwargs) -> None:
        super(ImageScreen, self).__init__(**kwargs)
        self.img_path: str = img_path
        self.picture: Image = Image.open(self.img_path)
        self.rotate_image()
        self.rescale_image()

    def rotate_image(self) -> None:
        if self.display.rotation % 180 == 90:
            self.height = self.display.width  # we swap height/width to rotate it to landscape!
            self.width = self.display.height
        else:
            self.width = self.display.width  # we swap height/width to rotate it to landscape!
            self.height = self.display.height

    def rescale_image(self) -> None:
        image_ratio = self.picture.width / self.picture.height
        screen_ratio = self.width / self.height
        if screen_ratio < image_ratio:
            scaled_width = self.picture.width * self.height // self.picture.height
            scaled_height = self.height
        else:
            scaled_width = self.width
            scaled_height = self.picture.height * self.width // self.picture.width
        self.picture = self.picture.resize((scaled_width, scaled_height), Image.BICUBIC)
        x = scaled_width // 2 - self.width // 2
        y = scaled_height // 2 - self.height // 2
        self.picture = self.picture.crop((x, y, x + self.width, y + self.height))
    
    def draw_screen(self) -> None:
        self.display.image(self.picture)
