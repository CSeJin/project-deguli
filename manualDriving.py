import os
import rospy
from std_msgs.msg import String
import time

# cmd = "python ~/app/talker.py "
cmd = "python ./test.py "


# 노드 초기화
rospy.init_node('manualDriving_publisher', anonymous=True)

 # 'hello' 토픽으로 메시지를 발행할 Publisher 생성
pub = rospy.Publisher('direction', String, queue_size=1)
rate = rospy.Rate(1)
msg = String()

def move_straight(self):
    # publishing
    msg = 'w'
    
    while not rospy.is_shutdown():
        pub.publish(msg)
        rate.sleep()

def turn_left(self):
    # publishing
    msg = 'a'
    
    while not rospy.is_shutdown():
        pub.publish(msg)
        rate.sleep()

def move_back(self):
    # publishing
    msg = 'x'
    
    while not rospy.is_shutdown():
        pub.publish(msg)
        rate.sleep()

def turn_right(self):
    # publishing
    msg = 'd'
    
    while not rospy.is_shutdown():
        pub.publish(msg)
        rate.sleep()

def stop_run(self):
    # publishing
    msg = 's'
    
    while not rospy.is_shutdown():
        pub.publish(msg)
        rate.sleep()


