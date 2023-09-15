#! /usr/bin/env python
import rospy
from std_msgs.msg import String
import os


def msg_callback(msg):
    cmd = "python3 ~/app/manualDriving_to_openCR.py " + str(msg)
    os.system(cmd)


if __name__ == '__main__':
    rospy.init_node('manualDriving_subscriber')
    sub = rospy.Subscriber('/direction', String, msg_callback, queue_size=1)
    
    rospy.spin()

