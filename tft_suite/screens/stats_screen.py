from tft_suite.screens.screen import Screen
import threading
import time
import subprocess


class StatsScreen(Screen):

    def __init__(self, **kwargs):
        super(StatsScreen, self).__init__(**kwargs)

    def run(self):
        t = threading.currentThread()
        rotation = 90
        padding = -2
        top = padding
        bottom = self.height - padding
        x = 0

        while getattr(t, "do_run", True):
            # Draw a black filled box to clear the image.
            self.draw.rectangle((0, 0, self.width, self.height), outline=0, fill=0)

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
            self.draw.text((x, y), IP, font=self.font, fill="#FFFFFF")
            y += self.font.getsize(IP)[1] + 5
            self.draw.text((x, y), CPU, font=self.font, fill="#FFFF00")
            y += self.font.getsize(CPU)[1] + 5
            self.draw.text((x, y), MemUsage, font=self.font, fill="#00FF00")
            y += self.font.getsize(MemUsage)[1] + 5
            self.draw.text((x, y), Disk, font=self.font, fill="#0000FF")
            y += self.font.getsize(Disk)[1] + 5
            self.draw.text((x, y), Temp, font=self.font, fill="#FF00FF")

            # Display image.
            self.display.image(self.image, rotation)
            time.sleep(0.1)
