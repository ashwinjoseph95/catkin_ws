#!/usr/bin/env python
import rospy
#from std_msgs.msg import String
import sys
sys.path.append('..')
from ros_basics_tutorials.msg import IoTSensor
import random

def move():
    pub = rospy.Publisher('iot_sensor_topic', IoTSensor, queue_size=10)
    rospy.init_node('iot_sensor_publisher_node', anonymous=True)
    rate = rospy.Rate(1)
    i=0
    while not rospy.is_shutdown():
        iotsensor= IoTSensor()
        iotsensor.id = 1
        iotsensor.name = "iot_parking_01"
        iotsensor.temperature = 24.33*(random.random()*2)
        iotsensor.humidity = 33.41*(random.random()*2)      
        print("Pose.x: ",iotsensor.id)
        print("iotsensor.name: ",iotsensor.name)
        print("iotsensor.temperature: ",iotsensor.temperature)
        print("iotsensor.humidity: ",iotsensor.humidity)
        rospy.loginfo("I publish")
        rospy.loginfo(iotsensor)
        pub.publish(iotsensor)
        rate.sleep()
        i=i+1

if __name__ == '__main__':
    try:
        move()
    except rospy.ROSInterruptException:
        pass
