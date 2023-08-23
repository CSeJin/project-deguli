import sys

from PyQt5 import Qt
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QApplication


# 제목
class Title(QLabel):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)

# 메인
class EmrCall(QMainWindow):
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
        layout_contents = QVBoxLayout()

        # 제목 설정
        title = Title("긴급호출")
        title.setAlignment(Qt.AlignHCenter)
        layout_title.addWidget(title)

        # 이미지 및 텍스트
        img = QPixmap("./assets/emr_light.png")
        emr_img = QLabel()
        emr_img.setPixmap(img)
        # emr_img.setGeometry(400,400,400,400)
        emr_img.setAlignment(Qt.AlignCenter)
        emr_txt = QLabel("관리자 호출 중")
        emr_txt.setAlignment(Qt.AlignCenter)

        layout_contents.addWidget(emr_img)
        layout_contents.addWidget(emr_txt)

        # 레이아웃 배치
        main_layout.addLayout(layout_title)
        main_layout.addLayout(layout_contents)

        self.setCentralWidget(main_widget)  # 중앙 위젯 설정
        self.resize(1024, 600)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = EmrCall()
    sys.exit(app.exec_())




