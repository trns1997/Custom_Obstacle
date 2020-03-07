#!/usr/bin/env python
 
import rospy
import random
import numpy as np
from std_msgs.msg import Float32MultiArray
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import PoseStamped

def callBack(msg):

    pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=1)
    
    goal = PoseStamped()
    goal.header.frame_id = "map"

    print(msg.data[0], msg.data[1])

    goal.pose.position.x = msg.data[0]
    goal.pose.position.y = msg.data[1]
    goal.pose.orientation.z = -0.7
    goal.pose.orientation.w = 0.7

    pub.publish(goal)

def main():
    rospy.init_node('move2pos')
    rospy.Subscriber("/rbt_trgt", Float32MultiArray, callBack)
    # Spin until ctrl + c
    rospy.spin()
 
if __name__ == '__main__':
    main()