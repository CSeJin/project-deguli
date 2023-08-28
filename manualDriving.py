import os

cmd = "python $HOME/application/talker.py"


def move_straight(self):
    # talker.py 파일 연결
    cmd_direction = cmd + " w"
    print(cmd_direction)

def turn_left(self):
    # talker.py 파일 연결
    cmd_direction = cmd + " a"
    print(cmd_direction)

def move_back(self):
    # talker.py 파일 연결
    cmd_direction = cmd + " x"
    print(cmd_direction)

def turn_right(self):
    # talker.py 파일 연결
    cmd_direction = cmd + " d"
    print(cmd_direction)

def stop_run(self):
    # talker.py 파일 연결
    cmd_direction = cmd + " s"
    print(cmd_direction)


