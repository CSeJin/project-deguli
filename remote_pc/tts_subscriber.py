import pyttsx3
from std_msgs.msg import String

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 130)
    engine.say(text)
    engine.runAndWait()

def call_text_to_speech(msg):
    text = "목적지를 " + str(msg.data) + "로 설정합니다."
    text_to_speech(text)

if __name__ == '__main__':
    try:
        rospy.Subscriber('/tts', String, call_text_to_speech, queue_Size=1)
        