import sys
import time
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QVBoxLayout, QLabel
from PyQt5 import QtGui, QtWidgets

import a.main


class LoadingDialog(QDialog):
    def __init__(self, parent=None):
        super(LoadingDialog, self).__init__(parent)
        self.setWindowTitle("")
        self.setWindowModality(Qt.ApplicationModal)
        self.setFixedSize(320, 200)
        
        self.label = QLabel("관리자가 권한 제어 중입니다.", self)
        self.label.setAlignment(Qt.AlignCenter)
        
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)
        
        # 창의 타이틀 바와 닫기 버튼을 숨깁니다.
        self.setWindowFlag(Qt.FramelessWindowHint)
        
        self.setupUi(self)
    
    def setupUi(self, LoadingDialog):
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        
        LoadingDialog.resize(400, 300)
        LoadingDialog.setStyleSheet("""background-color: #333333;
                                        color: white;""")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LoadingDialog.sizePolicy().hasHeightForWidth())
        LoadingDialog.setSizePolicy(sizePolicy)


class Worker(QThread):
    finished = pyqtSignal()
    
    def run(self):
        # 여기에 수행할 작업을 넣으세요
        time.sleep(5)  # 예를 들면 5초 동안의 작업을 시뮬레이션
        # 작업이 끝나면 시그널을 보냅니다.
        self.finished.emit()


# class MainWindow(QMainWindow):
#     def __init__(self):
#         super(MainWindow, self).__init__()
#         self.worker = None
#         self.setWindowTitle("로딩 테스트")
#         self.setGeometry(200, 200, 300, 200)
#
#         self.btn_home = QPushButton("Home", self)
#         self.btn_home.setGeometry(100, 75, 100, 50)
#         self.btn_home.clicked.connect(self.show_loading_dialog)
#
#         self.loading_dialog = None  # loading_dialog를 MainWindow 객체의 속성으로 설정
#
#         self.timer = QTimer(self)
#         self.timer.timeout.connect(self.handle_timeout)
#         self.timer.start(30000)  # 30초 타임아웃

def show_loading_dialog(window):
    loading_dialog = LoadingDialog(window)
    loading_dialog.setWindowModality(Qt.ApplicationModal)
    loading_dialog.show()
    QApplication.processEvents()
    
    # 메인 윈도우 비활성화
    window.setEnabled(False)
    
    # Worker 쓰레드를 생성하여 작업 시작
    worker = Worker()
    worker.finished.connect(lambda: hide_loading_dialog(loading_dialog, window))
    worker.run()


# 이전 코드에서 수정된 부분
def hide_loading_dialog(loading_dialog, window):
    loading_dialog.close()
    loading_dialog.deleteLater()  # 참조 삭제
    # 메인 윈도우 다시 활성화
    window.setEnabled(True)


def handle_timeout(self):
    print("제어 요청이 거부되었습니다")
    self.hide_loading_dialog()

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     mainWin = MainWindow()
#     mainWin.show()
#     sys.exit(app.exec_())
