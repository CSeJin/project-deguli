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


def getKey():
    if os.name == 'nt':
        timeout = 0.1
        startTime = time.time()
        while (1):
            if msvcrt.kbhit():
                if sys.version_info[0] >= 3:
                    return msvcrt.getch().decode()
                else:
                    return msvcrt.getch()
            elif time.time() - startTime > timeout:
                return ''
    
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''


def direction_callback(msg):
    try:
        if msg.data == 'w':
            linear_vel = 0.15
            angular_vel = 0
            print(msg.data)
        elif msg.data == 'x':
            linear_vel = -0.15
            angular_vel = 0
            print(msg.data)
        elif msg.data == 'd':
            linear_vel = 0
            angular_vel = 0.06
            print(msg.data)
        elif msg.data == 'a':
            linear_vel = 0
            angular_vel = -0.06
            print(msg.data)
        elif msg.data == 's':
            linear_vel = 0
            angular_vel = 0
            print(msg.data)
        else:
            print(e)
        
        twist = Twist()
        twist.linear.x = linear_vel
        twist.angular.z = angular_vel
        pub.publish(twist)
    
    except KeyboardInterrupt:
        print(e + ": pub to openCR")
    
    finally:
        twist = Twist()
        twist.linear.x = 0.0
        twist.angular.z = 0.0
        pub.publish(twist)


if __name__ == "__main__":
    if os.name != 'nt':
        settings = termios.tcgetattr(sys.stdin)
    
    # from_raspberryPi: raspberryPi로부터 이동 명령 subscribe
    rospy.init_node('manualDriving_subscriber', anonymous=True)
    rate = rospy.Rate(1)
    
    # to_openCR: openCR로 주행 명령 publishing
    rospy.init_node('turtlebot3_teleop')
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    turtlebot3_model = rospy.get_param("model", "burger")
    
    try:
        while not rospy.is_shutdown():
            # direction 토픽 subscribe
            sub = rospy.Subscriber('/direction', String, direction_callback, queue_size=1)
            rate.sleep()
    
    except KeyboardInterrupt:
        print(e)
    
    if os.name != 'nt':
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
