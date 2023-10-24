import threading

import tf
import paho.mqtt.client as mqtt


def check_position(self):
    global x, y
    try:
        (trans, rot) = tf_listener.lookupTransform('/map', '/base_footprint', rospy.Time(0))  # 현재 시간에 대한 로봇 위치 가져옴

        # x,y 좌표 확인
        x = trans[0]
        y = trans[1]

        # 현재위치 관제 서버로 전송
        send_position(x, y)
    except:
        print("현재위치 가져오기 실패")
        

def send_position(x, y):
    # Client 생성
    client = mqtt.Client()
    
    # Client 연결
    client.connect('223.195.194.41', 1883)
    # client.connect('broker.hivemq.com', 1883)
    
    # Topic 설정
    topic = "present_position"
    
    # 메시지 생성
    message = str(x)+", "+str(y)
    
    # publish 확인
    def on_publish(client, userdata, mid):
        print("현재위치 pusblish 완료:"+str(x)+", "+str(y))
    
    # publish callback 함수 등록
    client.on_publish = on_publish
    
    # QoS 2로 publish
    client.publish(topic, message, qos=0)
    
    # Client 종료
    client.disconnect()

def call_position(self):
    check_position()
    threading.Timer(5.0, call_position).start()
    
if __name__ == "__main__":
    call_position()