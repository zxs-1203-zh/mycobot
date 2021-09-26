from pymycobot.mycobot import MyCobot
import port
from pymycobot.genre import Angle


mc = MyCobot(port.port)
mc.send_angle(Angle.J1.value, 90, 10)

