# tft-suite

## Description
tft-suite is an active development library for creating and switching between different screens
on an Adafruit Mini PiTFT. Adafruit offers these displays in two sizes [(135x240)](https://www.adafruit.com/product/4393) and [(240x240)](https://www.adafruit.com/product/4484).
Both of these displays come with two small tactile buttons allowing users to interact with a raspberry pi or the display.

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [License](#license)

## Installation

```shell
sudo apt-get install ttf-dejavu
python -m pip install git+https://github.com/drewtchrist/tft-suite
```

## Usage
tft-suite offers a small handful of screens that should work right out of the box. Some of the
screens have code that has been adapted from AdaFruit's [guide here](https://learn.adafruit.com/adafruit-mini-pitft-135x240-color-tft-add-on-for-raspberry-pi),
such as the one that shows stats about the raspberry pi. To use one of the screens that comes 
with tft-suite, import the Display class and any screens you would like to use like below.

```python
from tft_suite.display import Display
from tft_suite.screens.stats_screen import StatsScreen

if __name__ == '__main__':
    Display([
        (StatsScreen, ())
    ]).start()
```

Alternatively, anyone can create their own custom Screen class if they'd like to 
display something that tft-suite doesn't offer! This process should be simplified
later on, but the example below should be enough to get someone started. 

```python
from tft_suite.screens.screen import Screen
import threading
import time

class HelloWorldScreen(Screen):

    def __init__(self, **kwargs):
        super(HelloWorldScreen, self).__init__(**kwargs)

    def draw_screen(self):
        rotation = 90
        self.draw.rectangle((0, 0, self.width, self.height), outline=0, fill=0)
        self.draw.text((0, 0), "Hello, World!", font=self.font, fill="#FF00FF")
        self.display.image(self.image, rotation)
```

After your screen is created, import it and add it to the list of Screens in your
Display class like the first example.

![tft-suite gif](https://drive.google.com/uc?export=view&id=1BJnZUrAmg03JISMqwGYimUwBA3INzrGA)

When the code is running, screens can be cycled through with either of the two buttons.
The backlight can be turned off by quickly pressing both buttons at the same time.

## License

