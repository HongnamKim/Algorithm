#include <stdio.h>

int main(void) {
  int a, b, c;
  int reward = 0;

  scanf("%d %d %d", &a, &b, &c);

  int nums[3] = {a, b, c};
  int max = nums[0];

  // case 1. all different
  if (a != b && b != c && a != c) {
    for (int i = 1; i < 3; i++) {
      if (max < nums[i]) {
        max = nums[i];
      }
    }
    reward = max * 100;
  }
  // case 2. all same
  else if (a == b && b == c) {
    reward = 10000 + a * 1000;
  }
  // case 3. 2 same, 1 different
  else {
    if (a == b || a == c) {
      reward = 1000 + a * 100;
    } else /* b == c*/ {
      reward = 1000 + b * 100;
    }
  }

  printf("%d", reward);

  return 0;
}