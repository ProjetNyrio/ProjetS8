from pyniryo import *

# Connecting to robot
robot = NiryoRobot("10.10.10.10")

# Activating connexion with Conveyor Belt
conveyor_id = robot.set_conveyor()
print(conveyor_id)
