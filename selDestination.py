import sys

from PyQt5 import Qt
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QApplication, QHBoxLayout, QPushButton, \
    QTabWidget


# 제목
class Title(QLabel):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)


def show_map(floor):  # 층별 지도 및 리스트 출력하는 func
    # 지도
    url = "./assets/map_" + floor + ".jpg"  # 이미지 url
    img = QPixmap(url)
    map_img = QLabel()
    map_img.setPixmap(img)
    # 리스트

    # 레이아웃 배치
    layout_contents = QHBoxLayout()
    layout_contents.addWidget(map_img)
    # 탭에 레이아웃 배치
    tab = QWidget()
    tab.setLayout(layout_contents)
    return tab


# 메인
class SelDestination(QMainWindow):
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
        layout_tabs = QHBoxLayout()

        # 제목 설정
        title = Title("목적지 설정")
        title.setAlignment(Qt.AlignHCenter)
        layout_title.addWidget(title)

        # 층 탭
        tabs = QTabWidget()
        tabs.addTab(show_map("1f"), "1층")
        tabs.addTab(show_map("2f"), "2층")
        tabs.addTab(show_map("3f"), "3층")
        tabs.addTab(show_map("4f"), "4층")
        tabs.addTab(show_map("5f"), "5층")
        tabs.addTab(show_map("6f"), "6층")
        layout_tabs.addWidget(tabs)  # 탭 배치

        # 레이아웃 배치
        main_layout.addLayout(layout_title)
        main_layout.addLayout(layout_tabs)

        self.setCentralWidget(main_widget)  # 중앙 위젯 설정
        self.resize(1024, 600)  # 사이즈 설정
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = SelDestination()
    sys.exit(app.exec_())
