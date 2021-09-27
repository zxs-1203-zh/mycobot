from pymycobot.mycobot import MyCobot
import port
import move
import threading
import time

mc = MyCobot(port.port)
threadMov = threading.Thread(target = move.mov2, args = (mc,))
threadMov.start()
while move.isMoving:
    print(mc.get_coords(), time.time())
threadMov.join()

