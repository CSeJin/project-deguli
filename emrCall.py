# tts 및 관제 업데이트, 정지
import pyttsx3


# tts
def text_to_speech(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 140)
    engine.say(text)
    engine.runAndWait()


# 주행 정지
