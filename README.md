# 2019.09.30-image-preprocessing

Goal: make <strong>AI number recognition</strong>(1 digit only), and participate in the competition, on 25 Oct 2019.

ToDoList:

    1. Extract image from video, for the training data
    2. Make deep learning to learn number recognition
    3. Make frontend to communicate with users
    4. Optimalize this preprocessing code with numpy and opencv.
    5. Make other programs for the competition

# 이미지 전처리

목표는 <strong>ai 숫자 인식기</strong>(한 자리 수) 만들어서, 박람회 출전하기. 운영일은 10/25 금요일.
일단 이미지 전치리는 대강 되어가니, 데이터 확보랑 딥러닝이랑 프론트엔드 모듈만 어떻게 만들면 될 거 같다.
한참 멀었네.

이미지 읽고 쓰는건 opencv 제공 함수를 썼다. 바이너리 읽어서 처리하는 건 구현하기 귀찮았다...

또, 사실 이런 처리해주는거 numpy나 opencv에서 굉장히 간단히 지원해준다.
그래도 뭔가 해보고 싶었다. 어째 위랑은 반대인데.
그 대가로 최적화를 버렸다. ㅡㅡ

결국 남은 할일

    1. 동영상에서 트레이닝에 쓸 이미지를 추출하는 코드 구현
    (사진 노가다해서 찍는 대신, 동영상으로 찍어서 프레임 단위로 분해할 계획)
    2. 딥러닝 코드 구현
    3. 부스에 올 체험자와 상호작용할 프론트엔드 구현
    4. (optionally)이미지 바이너리 읽고 쓰는 코드 구현
    5. 전처리 numpy랑 opencv로 최적화
    6. ...그 외 출전할 다른 프로그램 구상 및 제작

