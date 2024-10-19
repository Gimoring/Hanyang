"""
특수문자 
- 하나의 명령문을 여러 줄에 작성
    - 백 슬래기 \나 괄호() 사용
    - if문 사용 시에는 \만 사용
    - print(''' ------ ''')
- print() 함수를 이용하여 여러 줄을 작성
    - ''' ~ ''' 사용
"""

a = 1
b = 0

e = "a" + "b" + "c" + "d"

f = "a" + "b" + "c" + "d"

if a == True and b == False:
    print("haha")

print(
    """ I like
      the school"""
)

"""
리스트의 특징
    - 인덱스를 통해 검색이 가능.
    - 값의 추가, 삭제가 가능
    - 추가 : 리스트.append(value) -> add after the last element.
    - 삭제 : 리스트.remove(value) -> remove the element
        삭제 시 같은 값이 여러 개 있다면 맨 앞에 있는 것부터 삭제.
    - len(리스트변수) : 리스트 길이의 계산이 가능.
"""

"""
2교시 : 함수
    sum(), average()....
    - 프로그램에서 자주 사용되는 소스코드를 따로 한 번 만들어서 필요할 때마다 불러서 사용하는 기능
    - 함수의 장점
        - 소스코드가 중복되지 않아 간결해짐
        - 소스코드의 재사용이 편리함
    선언 def add(args...):
        return args1+ args2
    호출 add(params...)
"""
