#include <stdio.h>

int main(void) {
  int index;
  scanf("%d", &index);

  int a[index], b[index];

  for (int i = 0; i < index; i++) {
    scanf("%d %d", &a[i], &b[i]);
  }

  for (int i = 0; i < index; i++) {
    printf("%d\n", a[i] + b[i]);
  }
}