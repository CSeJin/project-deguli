import os


def move(self, objectName):
    # talker.py 파일 연결
    cmd = "python $HOME/application/talker.py"

    if objectName == "btn_up":
        cmd += "w"
    elif objectName == "btn_left":
        cmd += "a"
    elif objectName == "btn_down":
        cmd += "x"
    elif objectName == "btn_right":
        cmd += "d"
    elif objectName == "btn_stop":
        cmd += "s"
    else:
        print("전달 인자 없음")
        return

    print(cmd)
    os.system(cmd)