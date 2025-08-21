from pymycobot.mycobot import MyCobot
import port

def init(mc: MyCobot):
    degrees = [0, 0, 0, 0, 0, 0]
    mc.send_angles(degrees, 20)
    print("hello")

if __name__ == "__main__":
    mc = MyCobot(port.port)
    init(mc)

