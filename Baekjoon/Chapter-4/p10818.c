#include <stdio.h>

int main(void) {
  int index;
  scanf("%d", &index);

  int arr[index];

  for (int i = 0; i < index; i++) {
    scanf("%d", &arr[i]);
  }

  int min = arr[0], max = arr[0];

  for (int i = 0; i < index; i++) {
    if (min > arr[i]) {
      min = arr[i];
    }

    if (max < arr[i]) {
      max = arr[i];
    }
  }

  printf("%d %d", min, max);

  return 0;
}