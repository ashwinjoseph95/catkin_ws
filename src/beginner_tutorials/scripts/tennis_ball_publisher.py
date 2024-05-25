#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge

class ImagePublisher:
    def __init__(self):
        rospy.init_node('image_publisher', anonymous=True)
        self.image_pub = rospy.Publisher('/tennis_ball_image', Image, queue_size=10)
        self.bridge = CvBridge()

    def publish_images(self, video_path):
        cap = cv2.VideoCapture(video_path)

        rate = rospy.Rate(30)  # Set the publishing rate

        while not rospy.is_shutdown():
            ret, frame = cap.read()
            if not ret:
                break

            image_msg = self.bridge.cv2_to_imgmsg(frame, "bgr8")
            self.image_pub.publish(image_msg)

            rate.sleep()

        cap.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    try:
        image_publisher = ImagePublisher()
        video_path = "your_video_path.mp4"  # Change this to your video file path
        image_publisher.publish_images(video_path)
    except rospy.ROSInterruptException:
        pass