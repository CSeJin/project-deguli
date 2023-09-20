# tts 및 관제 업데이트, 정지
import rospy
from std_msgs.msg import String

# 노드 초기화
rospy.init_node('manualDriving_publisher', anonymous=True)


def emr():
    # tts
    pub_tts = rospy.Publisher('tts', String, queue_size=1)
    msg_tts = String('emr')
    pub_tts.publish(msg_tts)
    
    # 주행 정지
    # 'direction' 토픽으로 메시지를 발행할 Publisher 생성
    pub_stop = rospy.Publisher('direction', String, queue_size=1)
    msg_stop = String('s')
    pub_stop.publish(msg_stop)
