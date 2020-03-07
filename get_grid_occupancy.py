#!/usr/bin/env python
 
import rospy
import random
import numpy as np
from std_msgs.msg import Float32MultiArray
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import OccupancyGrid

def callBack(msg):
    print(len(msg.data))

def main():
    rospy.init_node('move2pos')
    rospy.Subscriber("/map", OccupancyGrid, callBack)
    # Spin until ctrl + c
    rospy.spin()
 
if __name__ == '__main__':
    main()