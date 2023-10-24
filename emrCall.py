# tts 및 관제 업데이트, 정지
import rospy
import pyttsx3
from PyQt5.QtCore import QTimer
from std_msgs.msg import String

# 노드 초기화
rospy.init_node('manualDriving_publisher', anonymous=True)


def emr_tts():
    # tts: 위급상황 알림
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    engine.say("위급상황입니다. 위급상황입니다.")
    engine.runAndWait()
    
    # 주행 정지
    # 'direction' 토픽으로 메시지를 발행할 Publisher 생성
    pub_stop = rospy.Publisher('direction', String, queue_size=1)
    msg_stop = String('s')
    pub_stop.publish(msg_stop)

# QTimer를 이용한 소리 지연
def delayed_sound():
    # 1000 밀리초 (1초) 후에 delayed_sound 함수 호출
    QTimer.singleShot(500, emr_tts)