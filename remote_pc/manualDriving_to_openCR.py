import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String
import sys, select, os

if os.name == 'nt':
    import msvcrt, time
else:
    import tty, termios

BURGER_MAX_LIN_VEL = 0.22
BURGER_MAX_ANG_VEL = 2.84

e = """
Communications Failed
"""

# 플래그 초기화
command_received = False
linear_vel = 0
angular_vel = 0


def direction_callback(msg):
    global command_received, linear_vel, angular_vel
    try:
        if msg.data == 'w':
            linear_vel = 0.07
            angular_vel = 0
            command_received = True
            print(msg.data + ", linear_vel: " + str(linear_vel))
        elif msg.data == 'x':
            linear_vel = -0.07
            angular_vel = 0
            command_received = True
            print(msg.data + ", linear_vel: " + str(linear_vel))
        elif msg.data == 'd':
            linear_vel = 0
            angular_vel = 0.10
            command_received = True
            print(msg.data + ", angular_vel: " + str(angular_vel))
        elif msg.data == 'a':
            linear_vel = 0
            angular_vel = -0.10
            command_received = True
            print(msg.data + ", angular_vel: " + str(angular_vel))
        elif msg.data == 's':
            linear_vel = 0
            angular_vel = 0
            command_received = True
            print(msg.data)
        else:
            print(e)
    
    except KeyboardInterrupt:
        print(e + ": pub to openCR")


if __name__ == "__main__":
    if os.name != 'nt':
        settings = termios.tcgetattr(sys.stdin)
    
    rospy.init_node('turtlebot3_teleop', anonymous=True)
    rate = rospy.Rate(10)
    
    try:
        while not rospy.is_shutdown():
            if command_received:
                # to_openCR: openCR로 주행 명령 publishing
                pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
                
                twist = Twist()
                twist.linear.x = linear_vel
                twist.angular.z = angular_vel
                pub.publish(twist)
                
                # 플래그 초기화
                command_received = False
            
            rate.sleep()
    
    except KeyboardInterrupt:
        print(e)
    
    if os.name != 'nt':
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
