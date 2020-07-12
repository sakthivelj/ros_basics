#!/usr/bin/env python
import rospy
from ros_service.srv import AddTwoInts
from ros_service.srv import AddTwoIntsRequest
from ros_service.srv import AddTwoIntsResponse


def handle_add_two_inits(req):

    print "Returning [%s + %s = %s]"%(req.a, req.b, (req.a + req.b))
    return AddTwoIntsResponse(req.a + req.b)

def add_two_ints_server():
    rospy.init_node('add_two_ints_server')
    s = rospy.Service('add_two_ints', AddTwoInts, handle_add_two_inits)
    print "Ready to add two ints."
    rospy.spin()

if __name__=="__main__":

    add_two_ints_server()
