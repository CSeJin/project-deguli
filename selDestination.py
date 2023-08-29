des_x, des_y = 0, 0


def assign_des(btn):
    print(btn.text())
    global des_x, des_y # 외부에서 전역 변수를 사용하기 위해 global 선언

    if btn.text() == "CT촬영실":

        des_x = 1  # db에서 조회한 좌표를 변수에 할당
        des_y = 1
    elif btn.text() == "비뇨기과":
        des_x = 1
        des_y = 2
    elif btn.text() == "비상계단":
        des_x = 1
        des_y = 3
    elif btn.text() == "이비인후과":
        des_x = 2
        des_y = 1
    elif btn.text() == "접수처":
        des_x = 2
        des_y = 2
    elif btn.text() == "치과":
        des_x = 2
        des_y = 3
    elif btn.text() == "화장실":
        des_x = 3
        des_y = 1
    elif btn.text() == "핵의학과":
        des_x = 3
        des_y = 2
    print(des_x, des_y)


def start_driving(btn):
    global des_x, des_y
    print(des_x, des_y)
    # 클릭 시 버튼 텍스트 전환
    if btn.text() == "주행시작":
        btn.setText("정지")
    elif btn.text() == "정지":
        btn.setText("주행시작")
    # 지정좌표로 이동할 수 있는 py파일에 연결


