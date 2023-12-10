# 데굴이:자율주행 휠체어 로봇
## 🦼 프로젝트 소개
병원 내 휠체어 이용 환자의 이동성 및 인력효율 개선을 위한 자율주행 휠체어 로봇 프로젝트

turtlebot3를 annotation하여 프로젝트 진행

<b> 역할: 수동주행 및 사용자 ui 구현 </b>

</br>

## 🦼 기술스택
python3, ROS1

ui: pyqt5
IDE: pycharm

</br>
  
## 🦼 기능(어플리케이션)
### 자율주행
- 목적지 선택 및 주행 시작 클릭 시 tts로 음성안내 및 서버로 목적지 publishing
- 서버에서 최적 경로를 연산하여 모터 제어 명령을 subscribe

<img src="https://github.com/CSeJin/project-deguli/assets/127668461/cc5306e1-e8b8-4806-b4aa-d1e274e137a4" width="400"> | (gif 첨부)

> 목적지 설정 클릭 -> 목적지 선택 -> 주행 시작 클릭
### 수동주행
- ui에서 버튼 클릭 시 해당 방향으로 주행하도록 모터에 명령
  
<img src="https://github.com/CSeJin/project-deguli/assets/127668461/4f247ae1-c6a7-4446-95ec-ff4fc10df8f8" width="400"> | (gif 첨부)

### 긴급호출
- 환자 위급상황 발생 시 해당 버튼을 클릭 -> 관제 측에 알림 전송 및 tts 음성안내
(gif 첨부)

</br>

## 🦼 파일설명
### runOnLaptop
> 노트북 환경에서 테스트용
### runOnTurtlebot3
- emrCall.py: 긴급호출 관련 메서드 관리 - tts, 관제 알림
- emrCall_ui.py: 긴급호출 페이지 ui
- loading.py: 관제 측에서 모터 제어 시 화면 비활성화를 위한 메서드 관리
- main.py: 어플리케이션의 동작 및 실행 관리
- mainPage_ui.py: 메인화면 페이지 ui
- manualDriving.py: 수동주행 관련 메서드 관리 - 모터 제어
- manualDriving_ui.py: 수동주행 페이지 ui
- selDestination.py: 자율주행 관련 메서드 관리 - 목적지, 서버 publishing
- selDestination_ui.py: 자율주행 페이지 ui


