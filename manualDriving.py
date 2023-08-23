import sys
from PyQt5 import Qt
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QMainWindow, QWidget, QVBoxLayout, QGridLayout, QPushButton, QApplication


# 제목
class Title(QLabel):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        # self.styleSheet("""
        #                 font-size: 30px;
        #                 font-weight: bold;
        #                 text-align: center;
        # """)
class DriveBtn(QPushButton):
    def __init__(self, parent=None):
        super().__init__( parent)

class manualDriving(QMainWindow):
    def __init__(self):
        super().__init__()
        self.set_style()
        self.init_ui()

    def set_style(self):
        with open("main-style.ui", 'r') as f:
            self.setStyleSheet(f.read())

    def init_ui(self):
        main_widget = QWidget()
        main_layout = QVBoxLayout(main_widget)

        # 위젯 배치용 레이아웃
        layout_title = QVBoxLayout()
        layout_contents = QGridLayout()

        # 제목 설정: layout_title
        title = Title("수동주행")
        title.setAlignment(Qt.AlignHCenter)
        layout_title.addWidget(title)

        # 버튼: layout_contents
        btn_up = DriveBtn()     # 전진
        btn_up.styleSheet('border-image:url("/assets/arrow_up.png");')
        layout_contents.addWidget(btn_up, 2, 0)
        btn_left = DriveBtn()   # 좌회전
        btn_left.styleSheet('border-image:url("/assets/arrow_left.png");')
        layout_contents.addWidget(btn_left, 1, 2)
        btn_stop = DriveBtn("정지")   # 정지
        layout_contents.addWidget(btn_stop, 2, 2)
        btn_right = DriveBtn()  # 우회전
        btn_right.styleSheet('border-image:url("/assets/arrow_right.png");')
        layout_contents.addWidget(btn_right, 3, 2)
        btn_down = DriveBtn()   # 후진
        btn_down.styleSheet('border-image:url("/assets/arrow_down.png");')
        layout_contents.addWidget(btn_down, 2, 0)

        # 레이아웃 배치
        main_layout.addLayout(layout_title)
        main_layout.addLayout(layout_contents)

        self.setCentralWidget(main_widget)  # 중앙 위젯 설정
        self.resize(1024, 600)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = manualDriving()
    sys.exit(app.exec_())