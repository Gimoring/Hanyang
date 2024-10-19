#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
    int game = 1;
    int red = 0;
    int sum = 0;

    while (game) {
        printf("주사위를 던지려면 Enter를 치세요.\n");
        getchar(); // 아무 입력 하나 받기.

        srand(time(0));
        int red = rand() % 6 + 1; // 1~6
        sum += red;
        printf("check sum = %d, red = %d", sum, red);
    }
}