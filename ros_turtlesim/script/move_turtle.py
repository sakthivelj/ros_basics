#!/usr/bin/env python
import rospy
import math
import time
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from std_srvs.srv import Empty

x = 0
y = 0
yaw = 0

def poseCallback(pose_message):
    global x
    global y, yaw
    x= pose_message.x
    y= pose_message.y
    yaw = pose_message.theta

def move(speed, distance):

    speed_publish = rospy.Publisher('/turtle1/cmd_vel', String, queue_size=10)
    rospy.init_node('move_turtle', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():

        twist = Twist()
        twist.linear.x = 1.0
        speed_publish.publish(twist)
        rate.sleep()

if __name__ == '__main__':
    try:
        move()
    except rospy.ROSInterruptException:
        pass
