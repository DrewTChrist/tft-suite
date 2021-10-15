import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tft-suite",
    version="0.1.0",
    author="Andrew Christiansen",
    author_email="andrewtaylorchristiansen@gmail.com",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/drewtchrist/tft-suite",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.6',
    install_requires=[
        'Adafruit-Blinka',
        'adafruit-circuitpython-busdevice',
        'adafruit-circuitpython-rgb-display',
        'Adafruit-PlatformDetect',
        'Adafruit-PureIO',
        'Pillow',
        'pyftdi',
        'pyserial',
        'pyusb',
        'rpi-ws281x',
        'RPi.GPIO',
        'sysv-ipc'
    ],
    entry_points={'console_scripts': [],},
)
