import threading
import time
import subprocess

from PIL import ImageFont
from cmd_parser import iwlist_parser


def stats(height, width, draw, image, display):
    t = threading.currentThread()
    font = ImageFont.truetype("usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
    rotation = 90
    padding = -2
    top = padding
    bottom = height - padding
    x = 0

    #while True:
    while getattr(t, "do_run", True):
        # Draw a black filled box to clear the image.
        draw.rectangle((0, 0, width, height), outline=0, fill=0)

        # Shell scripts for system monitoring from here:
        # https://unix.stackexchange.com/questions/119126/command-to-display-memory-usage-disk-usage-and-cpu-load
        cmd = "hostname -I | cut -d' ' -f1"
        IP = "IP: " + subprocess.check_output(cmd, shell=True).decode("utf-8")
        cmd = "top -bn1 | grep load | awk '{printf \"CPU Load: %.2f\", $(NF-2)}'"
        CPU = subprocess.check_output(cmd, shell=True).decode("utf-8")
        cmd = "free -m | awk 'NR==2{printf \"Mem: %s/%s MB  %.2f%%\", $3,$2,$3*100/$2 }'"
        MemUsage = subprocess.check_output(cmd, shell=True).decode("utf-8")
        cmd = 'df -h | awk \'$NF=="/"{printf "Disk: %d/%d GB  %s", $3,$2,$5}\''
        Disk = subprocess.check_output(cmd, shell=True).decode("utf-8")
        cmd = "cat /sys/class/thermal/thermal_zone0/temp |  awk '{printf \"CPU Temp: %.1f C\", $(NF-0) / 1000}'"  # pylint: disable=line-too-long
        Temp = subprocess.check_output(cmd, shell=True).decode("utf-8")

        # Write four lines of text.
        y = top
        draw.text((x, y), IP, font=font, fill="#FFFFFF")
        y += font.getsize(IP)[1] + 5
        draw.text((x, y), CPU, font=font, fill="#FFFF00")
        y += font.getsize(CPU)[1] + 5
        draw.text((x, y), MemUsage, font=font, fill="#00FF00")
        y += font.getsize(MemUsage)[1] + 5
        draw.text((x, y), Disk, font=font, fill="#0000FF")
        y += font.getsize(Disk)[1] + 5
        draw.text((x, y), Temp, font=font, fill="#FF00FF")

        # Display image.
        display.image(image, rotation)
        time.sleep(0.1)

def networks(height, width, draw, image, display):
    t = threading.currentThread()
    font = ImageFont.truetype("usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 12)
    rotation = 90
    padding = -2
    top = padding
    bottom = height - padding
    x = 0

    #while True:
    while getattr(t, "do_run", True):
        # Draw a black filled box to clear the image.
        draw.rectangle((0, 0, width, height), outline=0, fill=0)

        # Shell scripts for system monitoring from here:
        # https://unix.stackexchange.com/questions/119126/command-to-display-memory-usage-disk-usage-and-cpu-load
        #cmd = 'iwlist wlan0 scan | grep "ESSID:"'
        #sudo iwlist wlan0 scan | awk -F ':' '/ESSID:/ {if ($2 != "\"\""){print $2;}}'
        #cmd = r"""sudo iwlist wlan0 scan | awk -F ':' '/ESSID:/ {if ($2 != "\"\""){print $2;}}'"""
        cmd = 'iwlist wlan0 scan'
        nets = subprocess.check_output(cmd, shell=True).decode("utf-8")
        nets = '\n'.join([f"{x['ESSID']} - Key:{x['Encryption key']}" for x in iwlist_parser(nets)])

        # Write four lines of text.
        y = top
        #draw.text((x, y), nets, font=font, fill="#FFFFFF")
        draw.text((0, 0), nets, font=font, fill="#FFFFFF")

        # Display image.
        display.image(image, rotation)
        time.sleep(0.1)
