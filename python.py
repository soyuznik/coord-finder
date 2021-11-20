
import win32api
import time
import mouse

while True:
    if(mouse.is_pressed("left")):
        time.sleep(0.5)
        x, y = win32api.GetCursorPos()
        xy = str(x)+","+str(y)
        print(xy.replace(" ",""))
