from pyniryo import * 

robot = NiryoRobot("10.10.10.10")
joints_place_pose=[-1.57,-0.4,-0.5,0,-0.4,0]
joints_pick_pose=[0,-0.7,-0.5,0,-0.4,0]

for i in range(3):
	robot.move_joints(joints_pick_pose)
	robot.grasp_with_tool()
	robot.move_joints(joints_place_pose)
	robot.release_with_tool()
	joints_pick_pose[0]+=-0.2


robot.move_to_home_pose()
robot.set_learning_mode(True)
robot.close_connection()




