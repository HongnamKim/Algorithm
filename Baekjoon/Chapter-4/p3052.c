#include <stdio.h>

int main(void) {
  int input;
  int output[10];

  for (int i = 0; i < 10; i++) {
    scanf("%d", &input);
    output[i] = input % 42;
  }

  int count = 10;
  int checked = 0;

  // 비교 같은 숫자를 찾을 경우 -1로 바꿔서 체크 여부 표시
  // output[i]가 -1일 경우 확인한 숫자이므로 다음 순서로 넘어감.
  for (int i = 0; i < 9; i++) {
    if (output[i] == -1) {
      continue;
    }

    // i번째 뒤에 있는 숫자 중 같은 숫자가 있을 경우 전체 count에서 차감
    // -1로 바꾸어서 중복으로 체크를 막음.
    for (int j = i + 1; j < 10; j++) {
      if (output[i] == output[j]) {
        count--;
        output[j] = -1;
      }
    }
  }

  printf("%d", count);

  return 0;
}