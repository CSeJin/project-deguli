import pyttsx3

import selDestination_ui

des_x, des_y = 0, 0


def assign_des(btn, btn_list):
    print(btn.text())
    global des_x, des_y  # 외부에서 전역 변수를 사용하기 위해 global 선언

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

    # db에서 조회한 좌표를 변수에 할당
    if btn.text() == "CT촬영실":
        des_x = 1
        des_y = 1
    elif btn.text() == "비뇨기과":
        des_x = 1
        des_y = 2
    elif btn.text() == "비상계단":
        des_x = 1
        des_y = 3
    elif btn.text() == "이비인후과":
        des_x = 2
        des_y = 1
    elif btn.text() == "접수처":
        des_x = 2
        des_y = 2
    elif btn.text() == "치과":
        des_x = 2
        des_y = 3
    elif btn.text() == "화장실":
        des_x = 3
        des_y = 1
    elif btn.text() == "핵의학과":
        des_x = 3
        des_y = 2
    print(des_x, des_y)


def start_driving(btn):
    global des_x, des_y
    print(des_x, des_y)
    # 클릭 시 버튼 텍스트 전환
    if btn.text() == "주행시작":
        btn.setText("정지")
        # 탭 비활성화
        # selDestination_ui.tabs.setDisabled(True)
    elif btn.text() == "정지":
        btn.setText("주행시작")
        # 탭 활성화
        # selDestination_ui.tabs.setEnabled(True)
    else:
        btn.setText("주행시작")

    # 지정좌표로 이동할 수 있는 py파일에 연결

    # 주행 시작 알림
def text_to_speech(text):
        engine = pyttsx3.init()
        engine.setProperty("rate", 140)
        engine.say(text)
        engine.runAndWait()