#!/usr/bin/env python
 
import rospy
import random
import numpy as np
from std_msgs.msg import Float32MultiArray

def main():
    rospy.init_node('input_obs')
    pub = rospy.Publisher('/obs', Float32MultiArray, queue_size=2)
    rate = rospy.Rate(10) # 10hz
    arr = np.zeros(2)
    i = 0
    while not rospy.is_shutdown():
        arr[i%2] = raw_input()
        i = i+1
        if i == 2:
            i = 0
            print("Sent: " + str(arr))
            pub.publish(Float32MultiArray(data=arr))
        rate.sleep()

 
if __name__ == '__main__':
    main()
