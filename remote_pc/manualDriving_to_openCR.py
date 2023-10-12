#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String

rospy.init_node('turtlebot_controller', anonymous=True)

cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
move_cmd = Twist()


def control_robot(msg):
    rate = rospy.Rate(10)  # 10Hz로 루프 실행
    
    while not rospy.is_shutdown():
        if msg.data == 'w':
            # 전진
            move_cmd.linear.x = 0.05
            move_cmd.angular.z = 0.0
        elif msg.data == 'a':
            # 좌회전
            move_cmd.linear.x = 0.0
            move_cmd.angular.z = 0.3
        elif msg.data == 'd':
            # 우회전
            move_cmd.linear.x = 0.0
            move_cmd.angular.z = -0.3
        elif msg.data == 'x':
            # 후진
            move_cmd.linear.x = -0.05
            move_cmd.angular.z = 0.0
        elif current_command == 's':
            # 정지
            move_cmd.linear.x = 0.0
            move_cmd.angular.z = 0.0
        
        cmd_vel_pub.publish(move_cmd)
        rate.sleep()


if __name__ == '__main__':
    try:
        rospy.Subscriber('/direction', String, control_robot, queue_size=1)
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
