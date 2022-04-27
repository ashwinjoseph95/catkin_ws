#!/usr/bin/env python
import sys
import rospy
#from std_msgs.msg import String

from ros_basics_tutorials.srv import AddTwoInts
from ros_basics_tutorials.srv import AddTwoIntsRequest
from ros_basics_tutorials.srv import AddTwoIntsResponse

def add_two_ints_client(x,y):
    rospy.wait_for_service('add_two_ints')
    try:
        add_two_ints = rospy.ServiceProxy('add_two_ints',AddTwoInts)
        resp1=add_two_ints(x,y)
        return resp1.sum
    except rospy.ServiceException(e):
        print("Service Call Failed: {}".format(e)



if __name__=="__main__":
    rospy.init_node("add_two_ints_entcli")
    s=rospy.Service("add_two_ints", AddTwoInts, handle_add_two_ints)
    print("Ready to add two ints")
    rospy.spin()
