#!/usr/bin/env python

import sys
import rospy
from ros_essentials_cpp.srv import AddTwoInts
from ros_essentials_cpp.srv import AddTwoIntsRequest
from ros_essentials_cpp.srv import AddTwoIntsResponse

def calculate_area_client(x, y):
    rospy.wait_for_service('calculate_area')
    try:
        calculate_area = rospy.ServiceProxy('calculate_area', AddTwoInts)
        resp1 = calculate_area(x, y)
        return resp1.sum
    except rospy.ServiceException as e:
        print ("Service call failed: {}".format(e))

def usage():
    return "%s [x y]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    else:
        print (usage())
        sys.exit(1)
    print ("Requesting %s*%s"%(x, y))
    s = calculate_area_client(x, y)
    print ("%s * %s = %s"%(x, y, s))
