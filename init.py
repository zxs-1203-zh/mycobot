from pymycobot.mycobot import MyCobot

def init(mc: MyCobot):
    degrees = [0, 0, 0, 0, 0, 0]
    mc.send_angles(degrees, 20)

