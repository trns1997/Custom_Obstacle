#!/usr/bin/env python
 
import rospy
import random
import numpy as np
from std_msgs.msg import Float32MultiArray
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import OccupancyGrid
from map_msgs.msg import OccupancyGridUpdate

def callBack_1(msg):
    global res, orig_x, orig_y, width, height, occup
    res =  msg.info.resolution
    orig_x = msg.info.origin.position.x
    orig_y = msg.info.origin.position.y
    width = msg.info.width
    height = msg.info.height
    occup = msg.data
    sub_once.unregister()



def callBack_2(msg):
    pub = rospy.Publisher('/map', OccupancyGrid, queue_size=1)

    goal = OccupancyGrid()
    goal.header.frame_id = "map"

    goal.info.resolution = res
    goal.info.width = width
    goal.info.height = height
    goal.info.origin.position.x = orig_x
    goal.info.origin.position.y = orig_y
    goal.info.origin.position.z = 0
    goal.info.origin.orientation.x = 0
    goal.info.origin.orientation.y = 0
    goal.info.origin.orientation.z = 0
    goal.info.origin.orientation.w = 1

    data = np.asarray(occup)
    x = msg.data[0]
    y = msg.data[1]
    blk = width/(width*res)
    tran_x = abs(orig_x - x)
    tran_y = abs(orig_y - y)
    pos = int((width*tran_y*blk) + (tran_x*blk))
    data[pos:pos+2] = 100
    data[pos+width:pos+2+width] = 100
    data[pos-width:pos+2-width] = 100
    goal.data = data
    pub.publish(goal)

def main():
    global sub_once
    rospy.init_node('pub_occupancy')
    sub_once = rospy.Subscriber("/map", OccupancyGrid, callBack_1)
    rospy.Subscriber("/obs", Float32MultiArray, callBack_2)
    # Spin until ctrl + c
    rospy.spin()

 
if __name__ == '__main__':
    main()