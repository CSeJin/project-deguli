import sys

from PyQt5 import Qt
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QWidget


# 제목
class Title(QLabel):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        # self.styleSheet("""
        #                 font-size: 30px;
        #                 font-weight: bold;
        #                 text-align: center;
        # """)


# 버튼
class MainButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)


class EmrButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)


# =========== main ============ #
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.set_style()
        self.init_ui()

    def set_style(self):
        with open("main-style.ui", 'r') as f:
            self.setStyleSheet(f.read())

    def init_ui(self):
        main_widget = QWidget()  # 메인 위젯 생성
        main_layout = QVBoxLayout(main_widget)

        # 위젯 배치용 레이아웃
        layout_top = QVBoxLayout()
        layout_btn = QVBoxLayout()

        # top-bar
        title = Title("홈")
        title.setAlignment(Qt.AlignHCenter)
        layout_top.addWidget(title)

        # 버튼
        selDesBtn = MainButton("목적지 설정")
        manualDriving = MainButton("수동주행")
        emrCall = EmrButton("긴급호출")

        layout_btn.addWidget(selDesBtn)
        layout_btn.addWidget(manualDriving)
        layout_btn.addWidget(emrCall)

        main_layout.addLayout(layout_top)
        layout_top.addStretch(1)
        main_layout.addLayout(layout_btn)
        layout_btn.addStretch(1)

        self.setCentralWidget(main_widget)  # 중앙 위젯 설정
        self.resize(1024, 600)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = Main()
    sys.exit(app.exec_())
