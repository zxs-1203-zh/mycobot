from pymycobot.mycobot import MyCobot
from init import init
import port

mc = MyCobot(port.port)
init(mc)

while True:
    print(mc.get_coords())

