#!/usr/bin/env python

from ros_essentials_cpp.srv import AddTwoInts
from ros_essentials_cpp.srv import AddTwoIntsRequest
from ros_essentials_cpp.srv import AddTwoIntsResponse

import rospy

def handle_calculate_area(req):
    print ("Returning [%s * %s = %s]"%(req.a, req.b, (req.a * req.b)))
    return AddTwoIntsResponse(req.a * req.b)

def calculate_area():
    rospy.init_node('calculate_area_server')
    s = rospy.Service('calculate_area', AddTwoInts, handle_calculate_area)
    print ("Ready to multiply two ints.")
    rospy.spin()
    
if __name__ == "__main__":
    calculate_area_server()
