#include <stdio.h>

int main(void) {
  int people[30];
  int submit;
  int unSubmit[2];

  // 1부터 30까지 array 초기화
  // 제출 x == 0, 제출 o == 1로 저장
  for (int i = 0; i < 30; i++) {
    people[i] = 0;
  }

  // 제출한 번호가 입력되면, 해당 출석번호 제출로 표시
  for (int i = 0; i < 28; i++) {
    scanf("%d", &submit);
    people[submit - 1] = 1;
  }

  int j = 0;
  // 제출하지 않은 번호 탐색
  for (int i = 0; i < 30; i++) {
    if (people[i] == 0) {
      unSubmit[j] = i + 1;
      j++;
    }
  }

  if (unSubmit[0] > unSubmit[1]) {
    printf("%d\n%d", unSubmit[1], unSubmit[0]);

  } else {
    printf("%d\n%d", unSubmit[0], unSubmit[1]);
  }

  return 0;
}