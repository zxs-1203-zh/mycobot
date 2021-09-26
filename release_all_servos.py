from pymycobot.mycobot import MyCobot
import port

mc = MyCobot(port.port)
mc.release_all_servos()

