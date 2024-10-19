"""
복습: 총정리
1. 변수, 연산자 
    - 산술 연산자 : +, -, *, /, //(정수인 몫만 리턴), % 나머지.
    - 비교 연산자 : ==, <=, >=, ...
    - 논리 연산자 : and or not
2. 조건문 
3. 반복문
4. 반복문의 제어
5. 리스트 사용자 정의 함수
6. 다양한 모듈 - time(), random(), turtle() 모듈
turtle 움직이기
.home() / .ht() 원점 0,0 으로 이동, 커서를 화면에서 숨기기
.setup(x,y) / .setheading(n) x,y에 위치 세팅, 커서 머리 위치 정하기
.forward(이동할 걸음)
.backward(이동할 걸음)
.left(각도), .right 각도
.circle(반지름), .circle(반지름 각도)
.fillcolor('color')
begin_fill() ... end_fill() 채우고자 하는 도형이 있는 구간 앞 뒤에 써줌.
.shape('shape') 커서모양 바꾸기 (arrow, triangle, classic, turtle, square, circle)

"""

"""
4. 이벤트 사용하기
    1. 키에 의해 함수 내용 실행하기.
    turtle.onkeypress(함수, "키이름")
    2. 키 입력모드 시 사용 하는 중요 함수
    screen.t.getScreen() 스크린을 사용할 수 있또록 스크린 객체 가져옴
    screen.listen() 스크린이 이벤트를 감지하고 반응하도록 설정
    screen.mainloop() 스크린 유
"""

import turtle as t


def left():
    t.left(90)
    t.fd(100)


def right():
    t.right(90)
    t.fd(100)


def backwd():
    t.backward(100)


def forwd():
    t.fd(100)


s = t.getscreen()
s.onkeypress(left, "Left")
s.listen()
s.mainloop()


"""
lambda 익명 함수
사용법 f = lambda x,y : x+y
f(2,4)

map(함수, 처리할 리스트)
예 >> a = [1,2,3,4]
map(lambda x:x*2, a) => 2,4,6,8
   >> b=list(map(int, input().split())
    -> 여러 개의 값을 입력 후 (input())
    -> 정수로 변환한 후 (int())
    -> 여러 개 값을 분기기호 기준으로 분리하여 리스트 형태로 저장.(.split(), list())
in 
    - 특정 값이 리스트 안에 있는지 확인
    - 결과는 true or false
예 >> a = [1,2,3,4]
value = 3
result = value in a # True
"""
