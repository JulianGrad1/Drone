
import tello
import time
import keyboard

drone = tello.Tello()
# Intiser 
print("Start")
time.sleep(10)
drone.takeoff()

while True:
    if keyboard.is_pressed('left arrow'):
        drone.ccw(15)
    elif keyboard.is_pressed('right arrow'):
        drone.cw(15)
    elif keyboard.is_pressed('down arrow'):
        drone.down(20)
    elif keyboard.is_pressed('up arrow'):
        drone.up(20)
    elif keyboard.is_pressed('w'):
        drone.forward(50)
    elif keyboard.is_pressed('a'):
        drone.left(50)
    elif keyboard.is_pressed('s'):
        drone.back(50)
    elif keyboard.is_pressed('d'):
        drone.right(50)
    elif keyboard.is_pressed('l'):
        drone.land()
        drone.streamoff()
        break
    