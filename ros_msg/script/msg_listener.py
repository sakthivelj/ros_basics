#!/usr/bin/env python
import rospy
from ros_msg.msg import IoTSensor

def iot_sensor_callback(iot):
    rospy.loginfo("new IoT data recivied:(%d, %s, %.2f, %.2f)",iot.id,iot.name,iot.temperatue,iot.humidity)

rospy.init_node('iot_sensor_listener_node', anonymous=True)
rospy.Subscriber("iot_sensor_topic", IoTSensor, iot_sensor_callback)
rospy.spin()
