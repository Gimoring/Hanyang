"""
Condition :
use custom function 
1) def opening(): introduction for game / no return value
2) def character_choice(): choose the character / return the character number value 
3) def battle(a):
    a: the name of character, ex) input('choose your name')
    initial value of a and the monster : 100
    the energy of each character is between -30 ~ 30 random value for 5 times of battle
    if the energy of each character is above 0, print "음... 만만치 않군."
    if the energy of other character is under 0, print "해당 전투가 승" 
    if same and above 0, print "둘 다 승리자"
"""


def opening():
    print(
        """=========================
이 게임은 5회의 전투가 가능하며
전투를 통해 최종 우승자가 출력된다.
캐릭터와 몬스터의 에너지는 모두 100부터 시작되며
총 10회 전투 중
-30~30 사이의 임의의 에너지로 전투력이 변경된다.
어느쪽이든 에너지가 0보다 작아지면 게임이 끝나고
5회의 전투 이후에도 둘 다 에너지가 0보다 크면 둘 다 우승으로 결정한다.
====================="""
    )


opening()

num = character_choice()
if num == 1:
    battle("곰")
elif num == 2:
    battle("고양이")
elif num == 3:
    battle("강아지")
else:
    print("맞지 않는 캐릭터. 다시 선택 주세요")
    num = character_choice()
