import rospy
from geometry_msgs.msg import Twist
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


def makeSimpleProfile(output, input, slop):
    if input > output:
        output = min(input, output + slop)
    elif input < output:
        output = max(input, output - slop)
    else:
        output = input
    
    return output


if __name__ == "__main__":
    if os.name != 'nt':
        settings = termios.tcgetattr(sys.stdin)
    
    rospy.init_node('turtlebot3_teleop')
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    
    turtlebot3_model = rospy.get_param("model", "burger")
    
    try:
        while not rospy.is_shutdown():
            if sys.argv[1] == 'w':
                linear_vel = 0.22
                angular_vel = 0
            elif sys.argv[1] == 'x':
                linear_vel = -0.22
                angular_vel = 0
            elif sys.argv[1] == 'd':
                linear_vel = 0
                angular_vel = 1.5
            elif sys.argv[1] == 'a':
                linear_vel = 0
                angular_vel = -1.5
            elif sys.argv[1] == 's':
                linear_vel = 0
                angular_vel = 0
            
            twist = Twist()
            twist.linear.x = linear_vel
            twist.angular.z = angular_vel
            pub.publish(twist)
    
    except KeyboardInterrupt:
        pass
    
    finally:
        twist = Twist()
        twist.linear.x = 0.0
        twist.angular.z = 0.0
        pub.publish(twist)
    
    if os.name != 'nt':
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
