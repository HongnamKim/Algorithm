#include <stdio.h>

int main(void) {
  int arr[9];
  for (int i = 0; i < 9; i++) {
    scanf("%d", &arr[i]);
  }

  int index = 1, max = arr[0];

  for (int i = 0; i < 9; i++) {
    if (max <= arr[i]) {
      max = arr[i];
      index = i + 1;
    }
  }

  printf("%d\n", max);
  printf("%d", index);

  return 0;
}