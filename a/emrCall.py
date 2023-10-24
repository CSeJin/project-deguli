# tts 및 관제 업데이트, 정지
import pyttsx3
from PyQt5.QtCore import QTimer


# 노드 초기화
def emr_tts():
    # tts: 위급상황 알림
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    engine.say("위급상황입니다. 위급상황입니다.")
    engine.runAndWait()


# QTimer를 이용한 소리 지연
def delayed_sound():
    # 1000 밀리초 (1초) 후에 delayed_sound 함수 호출
    QTimer.singleShot(500, emr_tts)

