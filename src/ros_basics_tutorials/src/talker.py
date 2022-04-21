import rospy
#from std_msgs.msg import String
from geometry_msgs.msg import Twist, Pose

def move():
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        twist= Twist()
        twist.linear.y = -1.0
        twist.linear.x = -1.0
        pose=Pose()
        print("Pose.x: ",pose.x)
        print("Pose.y: ",pose.y)
        print("Pose.theta: ",pose.theta)
        rospy.loginfo(twist.linear.x)
        pub.publish(twist)
        rate.sleep()

if __name__ == '__main__':
    try:
        move()
    except rospy.ROSInterruptException:
        pass
