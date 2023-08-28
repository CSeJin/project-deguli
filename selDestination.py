des_x, des_y = 0, 0


def assign_des(btn):
    print(btn.text())
    if btn.text() == "CT촬영실":
        global des_x, des_y # 외부에서 전역 변수를 사용하기 위해 global 선언
        des_x = 1  # db에서 조회한 좌표를 변수에 할당
        des_y = 1
    print(des_x, des_y)


def start_driving(self):
    print(des_x, des_y)

    # 지정좌표로 이동할 수 있는 py파일에 연결


