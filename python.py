
import win32gui
import time

while True:
    time.sleep(0.5)
    x, y = win32gui.GetCursorPos()
    print(x, y)
