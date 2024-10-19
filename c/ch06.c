#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() 
{
    int game = 5;
    int red = 0;
    int blue = 0;
    int sum = 0;

    while(game)
    {
        printf("주사위를 던지려면 Enter를 치세요. \n");
        getchar(); // 소문자 받는 것.

        srand(time(0));
        int red = rand() % 6 + 1; // 1부터 6까지 랜덤 수 발생
        int blue = rand() % 6 + 1; // 1부터 6까지 랜덤 수 발생

        sum = red + blue;

        printf("합은 %d, red : %d blue : %d\n", sum, red, blue);
        if (sum > 9) {
            printf("백만장자가 되었네요... \n");
            break;
        }
        else
        {
            printf("거지가 될 것 같아요...슬퍼요\n");
        }
        game--;
        printf("기회는 %d번 남았어요...\n", game);
    } 
    return 0;
}