from pymycobot import MyCobot
import port
import time

mc = MyCobot(port.port)
print(mc.get_coords(), time.time())
