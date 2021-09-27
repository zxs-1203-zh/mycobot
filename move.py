from pymycobot.mycobot import MyCobot
from pymycobot.genre import Angle, Coord
import init
import time

isMoving = True

def mov1(mc : MyCobot):
    global isMoving
    isMoving = True
    init.init(mc)
    time.sleep(7)
    mc.send_angle(Angle.J1.value, 90, 30)
    time.sleep(5)
    mc.send_angle(Angle.J1.value, -90, 30)
    time.sleep(5)
    mc.send_angle(Angle.J1.value, 0, 30)
    time.sleep(5)
    mc.send_angle(Angle.J2.value, 90, 30)
    time.sleep(5)
    mc.send_angle(Angle.J2.value, -90, 30)
    time.sleep(5)
    mc.send_angle(Angle.J2.value, 0, 30)
    time.sleep(5)
    mc.send_angle(Angle.J3.value, 90, 30)
    time.sleep(5)
    mc.send_angle(Angle.J3.value, -90, 30)
    time.sleep(5)
    mc.send_angle(Angle.J3.value, 0, 30)
    time.sleep(5)
    mc.send_angle(Angle.J4.value, 90, 30)
    time.sleep(5)
    mc.send_angle(Angle.J4.value, -90, 30)
    time.sleep(5)
    mc.send_angle(Angle.J4.value, 0, 30)
    time.sleep(5)
    mc.send_angle(Angle.J5.value, 90, 30)
    time.sleep(5)
    mc.send_angle(Angle.J5.value, -90, 30)
    time.sleep(5)
    mc.send_angle(Angle.J5.value, 0, 30)
    time.sleep(5)
    mc.send_angle(Angle.J6.value, 90, 30)
    time.sleep(5)
    mc.send_angle(Angle.J6.value, -90, 30)
    time.sleep(5)
    mc.send_angle(Angle.J6.value, 0, 30)
    isMoving = False

def mov2(mc : MyCobot):
    global isMoving
    isMoving = True
    init.init(mc)
    time.sleep(7)
    mc.send_angle(Angle.J3.value, 45, 30)
    for index in range(10):
        time.sleep(5)
        mc.send_angle(Angle.J1.value, -150, 30)
        time.sleep(5)
        mc.send_angle(Angle.J1.value, 150, 30)
    isMoving = False

def mov3(mc : MyCobot):
    global isMoving
    isMoving = True
    init.init(mc)
    isMoving = False

