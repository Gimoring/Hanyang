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
        printf("�ֻ����� �������� Enter�� ġ����. \n");
        getchar(); // �ҹ��� �޴� ��.

        srand(time(0));
        int red = rand() % 6 + 1; // 1���� 6���� ���� �� �߻�
        int blue = rand() % 6 + 1; // 1���� 6���� ���� �� �߻�

        sum = red + blue;

        printf("���� %d, red : %d blue : %d\n", sum, red, blue);
        if (sum > 9) {
            printf("�鸸���ڰ� �Ǿ��׿�... \n");
            break;
        }
        else
        {
            printf("������ �� �� ���ƿ�...���ۿ�\n");
        }
        game--;
        printf("��ȸ�� %d�� ���Ҿ��...\n", game);
    } 
    return 0;
}