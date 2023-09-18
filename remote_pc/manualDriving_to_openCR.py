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


def direction_callback(msg):
    linear_vel = 0
    angular_vel = 0
    
    try:
        if msg.data == 'w':
            rate.sleep()
            linear_vel = 0.10
            angular_vel = 0
            print(msg.data+", linear_vel: "+str(linear_vel))
        elif msg.data == 'x':
            rate.sleep()
            linear_vel = -0.10
            angular_vel = 0
            print(msg.data+", linear_vel: "+str(linear_vel))
        elif msg.data == 'd':
            rate.sleep()
            linear_vel = 0
            angular_vel = 0.10
            print(msg.data+", angular_vel: "+str(angular_vel))
        elif msg.data == 'a':
            rate.sleep()
            linear_vel = 0
            angular_vel = -0.10
            print(msg.data+", angular_vel: "+str(angular_vel))
        elif msg.data == 's':
            rate.sleep()
            linear_vel = 0
            angular_vel = 0
            print(msg.data)
        else:
            print(e)
        
        # to_openCR: openCR로 주행 명령 publishing
        pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)

        twist = Twist()
        twist.linear.x = linear_vel
        twist.angular.z = angular_vel
        pub.publish(twist)
    
    except KeyboardInterrupt:
        print(e + ": pub to openCR")
        

if __name__ == "__main__":
    if os.name != 'nt':
        settings = termios.tcgetattr(sys.stdin)
    
    # from_raspberryPi: raspberryPi로부터 이동 명령 subscribe
    rospy.init_node('turtlebot3_teleop', anonymous=True)
    rate = rospy.Rate(1)
    
    try:
        while not rospy.is_shutdown():
            # direction 토픽 subscribe
            sub = rospy.Subscriber('/direction', String, direction_callback, queue_size=1)
    
    except KeyboardInterrupt:
        print(e)
    
    if os.name != 'nt':
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)