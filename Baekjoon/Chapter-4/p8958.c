#include <stdio.h>

// 연속으로 맞을 경우, 추가되는 점수가 증가하는 형식
// 연속으로 맞는 문제의 수를 count한 후, 틀렸을 때 다시 0으로 초기화
int main(void) {
  int N;
  scanf("%d", &N);

  int scores[N];
  for (int i = 0; i < N; i++) {
    scores[i] = 0;
  }
  
  int count = 0;

  for (int i = 0; i < N; i++) {
    char results[80];
    scanf("%s", results);
  

    for (int j = 0; j < 80; j++) {

      if (results[j] == '\0') {
        break;
      }

      if (results[j] == 'O') {
        scores[i] = scores[i] + 1 + count;
        count++;
      } else {
        count = 0;
      }
    }

    count = 0;
  }

  for (int i = 0; i < N; i++) {
    printf("%d\n", scores[i]);
  }
}