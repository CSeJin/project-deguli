import sys

from PyQt5 import Qt
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QApplication, QHBoxLayout, QPushButton, \
    QTabWidget, QScrollArea


# 제목
class Title(QLabel):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)


class ListBtn(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)


class StartBtn(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
    
    
def show_map(floor):  # 층별 지도 및 리스트 출력하는 func
    # 탭
    tab = QWidget()
    # 레이아웃
    layout_contents = QHBoxLayout()
    layout_map = QVBoxLayout()
    layout_lists = QVBoxLayout()
    # 지도
    url = "./assets/map_" + floor + ".jpg"  # 이미지 url
    img = QPixmap(url)
    map_img = QLabel()
    map_img.setPixmap(img)
    # 리스트
    lists = QScrollArea()
    lists_options = QVBoxLayout()  # 리스트 요소를 담을 레이아웃
    tab.layout = layout_lists
    if floor == "1f":
        btn1 = ListBtn("CT촬영실")
        btn2 = ListBtn("비상계단")
        btn3 = ListBtn("이비인후과")
        btn4 = ListBtn("접수처")
        btn5 = ListBtn("화장실")
        lists_options.addWidget(btn1)
        lists_options.addWidget(btn2)
        lists_options.addWidget(btn3)
        lists_options.addWidget(btn4)
        lists_options.addWidget(btn5)
        lists.setLayout(lists_options)
    elif floor == "2f":
        btn1 = ListBtn("비뇨기과")
        btn2 = ListBtn("산부인과")
        btn3 = ListBtn("의료영상관리실")
        btn4 = ListBtn("치과")
        btn5 = ListBtn("탈의실(남자)")
        btn6 = ListBtn("탈의실(여자)")
        btn7 = ListBtn("핵의학과")
        lists_options.addWidget(btn1)
        lists_options.addWidget(btn2)
        lists_options.addWidget(btn3)
        lists_options.addWidget(btn4)
        lists_options.addWidget(btn5)
        lists_options.addWidget(btn6)
        lists_options.addWidget(btn7)
        lists.setLayout(lists_options)
    # 레이아웃 배치
    layout_map.addWidget(map_img)  # layout_map에 지도 배치
    layout_contents.addLayout(layout_map)  # tab에 지도를 포함한 레이아웃 배치
    layout_lists.addWidget(lists)  # layout_lists에 scrollArea 배치
    layout_contents.addLayout(layout_lists)  # tab에 스크롤 리스트 배치
    # 탭에 레이아웃 배치
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

    def start_or_stop(self):
        if self.start_btn.text() == "주행시작":
            self.start_btn.setText("정지")
        elif self.start_btn.text() == "정지":
            self.start_btn.setText("주행시작")

    def init_ui(self):
        main_widget = QWidget()
        main_layout = QVBoxLayout(main_widget)

        # 위젯 배치용 레이아웃
        layout_title = QVBoxLayout()
        layout_tabs = QHBoxLayout()
        layout_start = QHBoxLayout()

        # 제목 설정
        self.title = Title("목적지 설정")
        self.title.setAlignment(Qt.AlignHCenter)
        layout_title.addWidget(self.title)

        # 층 탭
        self.tabs = QTabWidget()
        self.tabs.addTab(show_map("1f"), "1층")
        self.tabs.addTab(show_map("2f"), "2층")
        self.tabs.addTab(show_map("3f"), "3층")
        self.tabs.addTab(show_map("4f"), "4층")
        self.tabs.addTab(show_map("5f"), "5층")
        self.tabs.addTab(show_map("6f"), "6층")
        layout_tabs.addWidget(self.tabs)  # 탭 배치

        # 주행시작/정지 버튼
        self.start_btn = StartBtn("주행시작")
        self.start_btn.clicked.connect(self.start_or_stop)
        layout_start.addWidget(self.start_btn)

        # 레이아웃 배치
        main_layout.addLayout(layout_title)
        main_layout.addLayout(layout_tabs)
        main_layout.addLayout(layout_start)

        self.setCentralWidget(main_widget)  # 중앙 위젯 설정
        self.resize(1024, 600)  # 사이즈 설정
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = SelDestination()
    sys.exit(app.exec_())
