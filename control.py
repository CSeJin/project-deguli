import threading
import tf
import paho.mqtt.client as mqtt

x = 0
y = 0


def check_position():
    global x, y
    try:
        # 이 부분은 ROS에 종속된 부분이므로 별도의 환경에서 실행되지 않을 수 있습니다.
        # 필요한 ROS 패키지가 설치되어 있는지 확인해야 합니다.
        (trans, rot) = tf_listener.lookupTransform('/map', '/base_footprint', rospy.Time(0))
        
        # x, y 좌표 확인
        x = trans[0]
        y = trans[1]
        
        # 현재위치 관제 서버로 전송
        send_position(x, y)
    except Exception as e:
        print("현재위치 가져오기 실패:", e)


def send_position(x, y):
    try:
        # Client 생성
        client = mqtt.Client()
        
        # Client 연결
        client.connect('223.195.194.41', 1883)
        # client.connect('broker.hivemq.com', 1883)
        
        # Topic 설정
        topic = "present_position"
        
        # 메시지 생성
        message = u"{}, {}".format(x, y)

        
        # publish 확인
        def on_publish(client, userdata, mid):
            print("현재위치 publish 완료:" + str(x) + ", " + str(y))
        
        # publish callback 함수 등록
        client.on_publish = on_publish
        
        # QoS 2로 publish
        client.publish(topic, message, qos=0)
        
        # Client 종료
        client.disconnect()
    except Exception as e:
        print("오류 발생:", e)


def call_position():
    check_position()
    threading.Timer(5.0, call_position).start()


if __name__ == "__main__":
    tf_listener = tf.TransformListener()  # ROS에 종속된 부분이므로 적절한 환경에서 실행되어야 합니다.
    call_position()
