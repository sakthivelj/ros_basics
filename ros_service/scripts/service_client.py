#!/usr/bin/env python

import sys
import rospy
from ros_service.srv import AddTwoInts
from ros_service.srv import AddTwoIntsRequest
from ros_service.srv import AddTwoIntsResponse


def add_two_ints_client(x,y):
    
def usage():
    return "%s [x,y]"%sys.argv[0]

if __name__ == '__main__':

    if len(sys.argv) == 3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    else:
        print usage()
        sys.exit(1)
    print "Request %s+%s""%(x,y)
