from pyniryo import * 

robot = NiryoRobot("10.10.10.10")
robot.move_joints(0.5,0.5,0,0,0,0)
robot.move_to_home_pose()
robot.set_learning_mode(True)
robot.close_connection()


