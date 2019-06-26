#!/usr/bin/env python
import rospy
# from std_msgs.msg import Int32
from UWBlocation.msg import location

def callback(data):
	rospy.loginfo(data)
	# if (data.data < 20000000):
	# 	Location_x = data.data - 10000000
	# 	#rospy.loginfo("count0 = %d",count0)
	# elif(data.data > 30000000):
	# 	Location_y = data.data - 30000000
	# 	#rospy.loginfo("count2 = %d",count2)
	# else :
	# 	Location_z = data.data - 20000000
	# 	#rospy.loginfo("count1 = %d",count1)
def listener():

     # In ROS, nodes are uniquely named. If two nodes with the same
     # node are launched, the previous one is kicked off. The
     # anonymous=True flag means that rospy will choose a unique
     # name for our 'listener' node so that multiple listeners can
     # run simultaneously.
	rospy.init_node('UWBlocation_sub', anonymous=True)
	global Location_x
	global Location_y
	global Location_z
	rospy.Subscriber("UWB_location", location, callback)

     # spin() simply keeps python from exiting until this node is stopped
	rospy.spin()

if __name__ == '__main__':
	listener()
