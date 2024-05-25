#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class ImageSubscriber:
    def __init__(self):
        rospy.init_node('image_subscriber', anonymous=True)
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber('/tennis_ball_image', Image, self.image_callback)
        self.yellowLower =(30, 150, 100)
        self.yellowUpper = (50, 255, 255)

    def read_rgb_image(self, image_name, show):
        rgb_image = cv2.imread(image_name)
        if show: 
            cv2.imshow("RGB Image",rgb_image)
        return rgb_image

    def filter_color(self, rgb_image, lower_bound_color, upper_bound_color):
        #convert the image into the HSV color space
        hsv_image = cv2.cvtColor(rgb_image, cv2.COLOR_BGR2HSV)
        cv2.imshow("hsv image",hsv_image)

        #find the upper and lower bounds of the yellow color (tennis ball)
        yellowLower =(30, 150, 100)
        yellowUpper = (50, 255, 255)

        #define a mask using the lower and upper bounds of the yellow color 
        mask = cv2.inRange(hsv_image, lower_bound_color, upper_bound_color)

        return mask

    def getContours(self, binary_image):      
        #_, contours, hierarchy = cv2.findContours(binary_image, 
        #                                          cv2.RETR_TREE, 
        #                                           cv2.CHAIN_APPROX_SIMPLE)
        _, contours, hierarchy = cv2.findContours(binary_image.copy(), 
                                                cv2.RETR_EXTERNAL,
                                                cv2.CHAIN_APPROX_SIMPLE)
        return contours


    def draw_ball_contour(self, binary_image, rgb_image, contours):
        black_image = np.zeros([binary_image.shape[0], binary_image.shape[1],3],'uint8')
        
        for c in contours:
            area = cv2.contourArea(c)
            perimeter= cv2.arcLength(c, True)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            if (area>100):
                cv2.drawContours(rgb_image, [c], -1, (150,250,150), 1)
                cv2.drawContours(black_image, [c], -1, (150,250,150), 1)
                cx, cy = self.get_contour_center(c)
                cv2.circle(rgb_image, (cx,cy),(int)(radius),(0,0,255),1)
                cv2.circle(black_image, (cx,cy),(int)(radius),(0,0,255),1)
                cv2.circle(black_image, (cx,cy),5,(150,150,255),-1)
                print ("Area: {}, Perimeter: {}".format(area, perimeter))
        print ("number of contours: {}".format(len(contours)))
        cv2.imshow("RGB Image Contours",rgb_image)
        cv2.imshow("Black Image Contours",black_image)

    def get_contour_center(self, contour):
        M = cv2.moments(contour)
        cx=-1
        cy=-1
        if (M['m00']!=0):
            cx= int(M['m10']/M['m00'])
            cy= int(M['m01']/M['m00'])
        return cx, cy

    def image_callback(self, data):
        cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")

        # # Apply ball detection algorithm (Example: using OpenCV's HoughCircles)
        # gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
        # circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20,
        #                            param1=50, param2=30, minRadius=0, maxRadius=0)

        # if circles is not None:
        #     circles = circles[0]
        #     for circle in circles:
        #         x, y, r = circle
        #         cv2.circle(cv_image, (x, y), r, (0, 255, 0), 4)
        rgb_image = self.read_rgb_image(data, True)
        binary_image_mask = self.filter_color(rgb_image, self.yellowLower , self.yellowUpper)
        contours = self.getContours(binary_image_mask)
        self.draw_ball_contour(binary_image_mask, rgb_image,contours)

        cv2.imshow("Tennis Ball Detection", cv_image)
        cv2.waitKey(1)

if __name__ == '__main__':
    try:
        image_subscriber = ImageSubscriber()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
