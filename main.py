import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow) :
    def __init__(self) :
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

        # 버튼에 페이지 연결
        self.ui_mainPage.btn_selDes.clicked.connect(self.show_selDestination)
        self.ui_mainPage.btn_manDriving.clicked.connect(self.show_manualDriving)
        self.ui_mainPage.btn_emrCall.clicked.connect(self.show_emrCall)
        # 홈 버튼 연결
        self.ui_selDestination.btn_home.clicked.connect(self.show_mainPage)
        self.ui_manualDriving.btn_home.clicked.connect(self.show_mainPage)
        self.ui_emrCall.btn_home.clicked.connect(self.show_mainPage)
        # 긴급 호출 버튼 연결
        self.ui_selDestination.btn_emrCall.clicked.connect(self.show_emrCall)
        self.ui_manualDriving.btn_emrCall.clicked.connect(self.show_emrCall)


        # 초기 화면 설정
        self.setCentralWidget(self.stacked_widget)

    def show_mainPage(self):
        # selDestination 페이지로 전환
        print("!")
        self.stacked_widget.setCurrentIndex(0)
        self.current_page_index = 0
    def show_selDestination(self):
        # selDestination 페이지로 전환
        print("!")
        self.stacked_widget.setCurrentIndex(1)
        self.current_page_index = 1

    def show_manualDriving(self):
        # selDestination 페이지로 전환
        self.stacked_widget.setCurrentIndex(2)
        self.current_page_index = 2

    def show_emrCall(self):
        # selDestination 페이지로 전환
        self.stacked_widget.setCurrentIndex(3)
        self.current_page_index = 3

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass()

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
