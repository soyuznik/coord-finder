import win32api
import time

from PIL import ImageGrab
import mouse

import pyperclip
import keyboard


def getColor(x,y):
    rgb = ImageGrab.grab().load()[x, y]
    return rgb;

while True:
    if(mouse.is_pressed("left")):
        if(keyboard.is_pressed('ctrl')):
            time.sleep(0.5)
            x, y = win32api.GetCursorPos()
            xy = str(x) + "," + str(y)
            xy.replace(' ', '');

            x1 = f"// Coords-> {xy}\n"

            x, y, z = getColor(x, y)
            x2 = f"// Color-> {x, y, z}\n"

            x = round(x / 255, 3);
            y = round(y / 255, 3);
            z = round(z / 255, 3);
            x3 = f"// Color(NDC)-> {x, y, z}\n"

            pyperclip.copy(x1 + x2 + x3)




