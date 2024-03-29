#include <stdio.h> 
#include <stdlib.h> 
#include <time.h>  

int main()
{
	int com; // 컴퓨터가 낸 값을 저장 
	int user; // 사용자가 낸 값을 저장 
	int a[3] = { 0, }; // 게임의 결과를 저장 0은 종료, 1은 승리, 2는 무승부, 3은 패배
	int b; // 승률 계산
	double winRate = 0; //승률
	int cnt = 0; // 게임의 횟수를 저장 하고 0으로 초기화
	srand((unsigned)time(NULL)); // rand 함수의 결과가 매번 다르도록 시드값을 지정(가위 바위 보 결과)

	while (1) // 사용자가 종료할 때 까지 반복 
	{
		com = rand() % 3 + 1; // 1~3 값 중 하나를 저장 
		printf("**************** 가위 바위 보  ****************\n");
		printf("(1. 가위 _ 2. 바위 _ 3. 보 _ 0. 종료)\n\n");
		printf("원하는 손을 입력해주세요 : ");
		scanf_s("%d", &user);
		if (user > 0 && user < 4) // 사용자가 1~3 값을 입력했을 경우 
		{
			cnt++; // 정상적인 입력의 경우 게임 횟수를 증가 
			// 컴퓨터, 사용자가 낸 값에 따라 가위, 바위, 보 중 출력할 값을 선택 
			printf("\n컴퓨터 : %s\n", (com == 1 ? "가위" : com == 2 ? "바위" : "보"));
			printf("사용자 : %s\n\n", (user == 1 ? "가위" : user == 2 ? "바위" : "보"));
			if (com == user) // 컴퓨터의 값과 사용자의 값이 같으면 비기는 경우 
			{
				printf("무승부 \n\n");
				a[1]++; // 무승부 횟수를 증가 
			}
			else if (((com == 1) && (user == 3)) ||
				((com == 2) && (user == 1)) ||
				((com == 3) && (user == 2)))
			{
				printf("패배\n\n");
				a[2]++; // 패배 횟수를 증가 
			}
		}
	}
}
