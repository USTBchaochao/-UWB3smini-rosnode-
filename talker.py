#!/usr/bin/env python
#####license removed for brevity
import rospy
from std_msgs.msg import Int32
import serial
import numpy
import time

port = serial.Serial('/dev/ttyACM0',115200)
#print(port.is_open)

x1 ,y1 ,z1= 0 , 0 , 0
x2 ,y2 ,z2= 4700 , 0 , 0
x3 ,y3 ,z3= 0 , 14000 , 0
x4 ,y4 ,z4= 4700 , 14000 , 1850

Mitrax_a = numpy.array([[-2*(x1-x2),2*(y1-y2),2*(z1-z2)],[-2*(x1-x3),2*(y1-y3),2*(z1-z3)],[-2*(x1-x4),2*(y1-y4),2*(z1-z4)]])

def read_1():
    read1 = port.read(1)
    read1 = str(read1)
    read1 = read1[0]
    return read1

def read_3():
    read3 = port.read(3)
    read3 = str(read3)
    read3 = read3[2:5]
    return read3

def read_all():
    read_all = port.read(61)
    return read_all

def talker():
	pub = rospy.Publisher('UWB_location', Int32, queue_size=10)
	rospy.init_node('talker', anonymous=True)
	rate = rospy.Rate(100000) 
	Location_x = 0
	Location_y = 0
	Location_z = 0
	while not rospy.is_shutdown():   
		read1 = read_1()
		if (read1 == 'm'):
			read2 = read_1()
			if (read2 == 'c'):
			    	read3 = read_3()
				print(read3)
				if (read3 == 'f'):
					read = read_all()
					distanceA = read[1:9]
					distanceB = read[10:18]
					distanceC = read[19:27]
					distanceD = read[28:36]

					distanceA = 0.98922 * int(distanceA, 16) - 525.304
					distanceA = 1.0024335 * distanceA + 2.99432
					#distancaA = 3*10**(-11)*(distanceA)**3-10**(-6)*(distanceA)**2+1.0105*distanceA-5.4992
					rospy.loginfo("disA = %d",distanceA)

					distanceB = 0.98922 * int(distanceB, 16) - 525.304
					distanceB = 1.0024335 * distanceB + 2.99432
					#distancaB = 3*10**(-11)*(distanceB)**3-10**(-6)*(distanceB)**2+1.0105*distanceB-5.4992
					rospy.loginfo("disB = %d",distanceB)

					distanceC = 0.98922 * int(distanceC, 16) - 525.304
					distanceC = 1.0024335 * distanceC + 2.99432
					#distancaA = 3*10**(-11)*(distanceC)**3-10**(-6)*(distanceC)**2+1.0105*distanceC-5.4992
					rospy.loginfo("disC = %d",distanceC)

					distanceD = 0.98922 * int(distanceD, 16) - 525.304
					distanceD = 1.0024335 * distanceD + 2.99432
					#distancaA = 3*10**(-11)*(distanceD)**3-10**(-6)*(distanceD)**2+1.0105*distanceD-5.4992
					rospy.loginfo("disD = %d",distanceD)
					rospy.loginfo("--------------------")

					u1 = distanceB ** 2 - distanceA ** 2 - x2 ** 2 + x1 ** 2 - y2 ** 2 + y1 ** 2 - z2 ** 2 + z1 ** 2
					u2 = distanceC ** 2 - distanceA ** 2 - x3 ** 2 + x1 ** 2 - y3 ** 2 + y1 ** 2 - z3 ** 2 + z1 ** 2
					u3 = distanceD ** 2 - distanceA ** 2 - x4 ** 2 + x1 ** 2 - y4 ** 2 + y1 ** 2 - z4 ** 2 + z1 ** 2
					Mitrax_b = numpy.array([[u1], [u2], [u3]])

					X0 = Mitrax_a.T
					X1 = (X0*Mitrax_a)
					X1 = numpy.linalg.inv(X1)
					X = X1 * X0 * Mitrax_b

					Location_x = X[0,0] + 10000000
					Location_y = X[1,1] + 20000000
					Location_z = X[2,2] + 30000000

					rospy.loginfo(Location_x)
					rospy.loginfo(Location_y)
					rospy.loginfo(Location_z)
		rate.sleep()

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
