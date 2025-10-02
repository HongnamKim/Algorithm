#include <stdio.h>

int main(void) {
  int index;
  scanf("%d", &index);

  int arr[index];
  for (int i = 0; i < index; i++) {
    scanf("%d", &arr[i]);
  }

  int target, count = 0;
  scanf("%d", &target);

  for (int i = 0; i < index; i++) {
    if (arr[i] == target) {
      count++;
    }
  }

  printf("%d", count);

  return 0;
}