import sys
from functools import partial

from manualDriving import move_straight, turn_left, move_back, turn_right, stop_run
from selDestination import assign_des, start_driving
from PyQt5.QtWidgets import *
from PyQt5 import uic


# 화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow):
    def __init__(self):
        super().__init__()

        # UI 파일 로드
        self.ui_mainPage = uic.loadUi("mainPage.ui")
        self.ui_selDestination = uic.loadUi("selDestination.ui")
        self.ui_manualDriving = uic.loadUi("manualDriving.ui")
        self.ui_emrCall = uic.loadUi("emrCall.ui")

        # UI 페이지 전환을 위한 QStackedWidget 생성
        self.stacked_widget = QStackedWidget(self)
        self.stacked_widget.addWidget(self.ui_mainPage)
        self.stacked_widget.addWidget(self.ui_selDestination)
        self.stacked_widget.addWidget(self.ui_manualDriving)
        self.stacked_widget.addWidget(self.ui_emrCall)

        # 현재 페이지 인덱스 기록
        self.current_page_index = 0

        #버튼 변수 정의
        self.btn_selDes = self.ui_mainPage.btn_selDes            # 메인페이지 - 목적지설정
        self.btn_manDriving = self.ui_mainPage.btn_manDriving    # 메인페이지 - 수동주행
        self.btn_emrCall = self.ui_mainPage.btn_emrCall          # 메인페이지 - 긴급호출
        self.btn1_1f = self.ui_selDestination.btn1_1f    # 목적지설정 - 1층-1
        self.btn2_1f = self.ui_selDestination.btn2_1f    # 목적지설정 - 1층-2
        self.btn3_1f = self.ui_selDestination.btn3_1f    # 목적지설정 - 1층-3
        self.btn4_1f = self.ui_selDestination.btn4_1f    # 목적지설정 - 1층-4
        self.btn5_1f = self.ui_selDestination.btn5_1f    # 목적지설정 - 1층-5
        self.btn6_1f = self.ui_selDestination.btn6_1f    # 목적지설정 - 1층-6
        self.btn7_1f = self.ui_selDestination.btn7_1f    # 목적지설정 - 1층-7
        self.btn8_1f = self.ui_selDestination.btn8_1f    # 목적지설정 - 1층-8
        self.btn_start = self.ui_selDestination.btn_start    # 목적지설정 - 주행시작
        # 버튼에 페이지 연결
        self.btn_selDes.clicked.connect(self.show_selDestination)
        self.btn_manDriving.clicked.connect(self.show_manualDriving)
        self.btn_emrCall.clicked.connect(self.show_emrCall)
        # 홈 버튼 연결
        self.ui_selDestination.btn_home.clicked.connect(self.show_mainPage)
        self.ui_manualDriving.btn_home.clicked.connect(self.show_mainPage)
        self.ui_emrCall.btn_home.clicked.connect(self.show_mainPage)
        # 목적지 설정
        self.btn1_1f.clicked.connect(lambda: self.call_assign_des(self.btn1_1f))
        self.btn2_1f.clicked.connect(partial(self.call_assign_des, btn=self.btn2_1f))
        self.btn3_1f.clicked.connect(partial(self.call_assign_des, btn=self.btn3_1f))
        self.btn4_1f.clicked.connect(partial(self.call_assign_des, btn=self.btn4_1f))
        self.btn5_1f.clicked.connect(partial(self.call_assign_des, btn=self.btn5_1f))
        self.btn6_1f.clicked.connect(partial(self.call_assign_des, btn=self.btn6_1f))
        self.btn7_1f.clicked.connect(partial(self.call_assign_des, btn=self.btn7_1f))
        self.btn8_1f.clicked.connect(partial(self.call_assign_des, btn=self.btn8_1f))
        self.btn_start.clicked.connect(lambda: self.call_start_driving(self.btn_start))
        # 긴급 호출 버튼 연결
        self.ui_selDestination.btn_emrCall.clicked.connect(self.show_emrCall)
        self.ui_manualDriving.btn_emrCall.clicked.connect(self.show_emrCall)
        # 수동주행
        self.ui_manualDriving.btn_up.clicked.connect(move_straight)
        self.ui_manualDriving.btn_left.clicked.connect(turn_left)
        self.ui_manualDriving.btn_down.clicked.connect(move_back)
        self.ui_manualDriving.btn_right.clicked.connect(turn_right)
        self.ui_manualDriving.btn_stop.clicked.connect(stop_run)

        # 초기 화면 설정
        self.setCentralWidget(self.stacked_widget)

    def show_mainPage(self):
        # selDestination 페이지로 전환
        print(self.ui_selDestination.btn_home.text())
        self.stacked_widget.setCurrentIndex(0)
        self.current_page_index = 0

    def show_selDestination(self):
        # selDestination 페이지로 전환
        print("목적지 설정")
        self.stacked_widget.setCurrentIndex(1)
        self.current_page_index = 1

    def show_manualDriving(self):
        # manualDriving 페이지로 전환
        print("수동주행")
        self.stacked_widget.setCurrentIndex(2)
        self.current_page_index = 2

    def show_emrCall(self):
        # emrCall 페이지로 전환
        print("긴급호출")
        self.stacked_widget.setCurrentIndex(3)
        self.current_page_index = 3

    def call_assign_des(self,btn):
        print("call_assign_des")
        assign_des(btn)

    def call_start_driving(self, btn):
        print("call_start_driving")
        start_driving(btn)


if __name__ == "__main__":
    # QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    # WindowClass의 인스턴스 생성
    myWindow = WindowClass()

    # 프로그램 화면을 보여주는 코드
    myWindow.show()

    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
