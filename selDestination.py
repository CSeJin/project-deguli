import time
import pyttsx3
import selDestination_ui
import rospy
from std_msgs.msg import String


des_x, des_y = 0, 0
msg = String()


def assign_des(btn, btn_list):
    print(btn.text())
    global des_x, des_y, msg  # 외부에서 전역 변수를 사용하기 위해 global 선언
    
    # 모든 버튼의 styleSheet를 초기화하는 코드 필요
    for other_btn_name in btn_list:
        other_btn = getattr(selDestination_ui.Ui_selDestination, other_btn_name)
        other_btn.setStyleSheet("""
                background-color: #cfe3ac;
                text-align: left;
                padding: 5px;
                padding-left: 20px;
                border: none;
            """)
    
    # 클릭한 버튼의 배경색상 변경
    btn.setStyleSheet("""
                        background-color: #a1c464;
                        text-align: left;
                        padding: 5px;
                        padding-left: 20px;
                        border: none;
    """)
    
    # 'direction' 토픽으로 메시지를 발행할 Publisher 생성
    pub = rospy.Publisher('rockstar', String, queue_size=1)
    
    # 목적지별 좌표를 저장할 publisher 전송
    if btn.text() == "CT촬영실":
        msg = '2'
        pub.publish(msg)
    elif btn.text() == "비뇨기과":
        msg = '1'
        pub.publish(msg)
    elif btn.text() == "이비인후과":
        msg = '3'
        pub.publish(msg)
    elif btn.text() == "접수처":
        msg = '0'
        pub.publish(msg)
    elif btn.text() == "치과":
        des_x = 2
        des_y = 3
    elif btn.text() == "화장실":
        des_x = 3
        des_y = 1
    print(msg)
    msg_text=btn.text()


def start_driving(btn):
    global des_x, des_y, msg, msg_tts
    print(des_x, des_y)
    
    if btn.text() == "주행시작":
        # navigation 시작 토픽 생성 및 전송
        pub = rospy.Publisher('start', String, queue_size=1)
        msg = 'start'
        pub.publish(msg)
        # 탭 비활성화
        # selDestination_ui.tabs.setDisabled(True)
        
        #### pub 확인용으로 주석처리####
        # tts(음성안내) publishing
        pub_tts = rospy.Publisher('tts', String, queue_size=1)
        pub_tts.publish(msg_tts)


        #### pub 확인용으로 주석처리####
        # tts(음성안내)
        #text="목적지를 "+btn.text()+"로 설정합니다."
        #text_to_speech(text)
        #time.sleep(1)
        # 클릭 시 버튼 텍스트 전환
        #btn.setText("정지")

    elif btn.text() == "정지":
        # tts(음성안내)
        text = "주행을 종료합니다."
        text_to_speech(text)
        time.sleep(1)
        # 클릭 시 버튼 텍스트 전환
        btn.setText("주행시작")
        # 탭 활성화
        # selDestination_ui.tabs.setEnabled(True)
    else:
        btn.setText("주행시작")
    
    # 지정좌표로 이동할 수 있는 py파일에 연결
    
    # 주행 시작 알림.


def text_to_speech(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 140)
    engine.say(text)
    engine.runAndWait()