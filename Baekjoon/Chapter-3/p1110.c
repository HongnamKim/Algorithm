#include <stdio.h>

int main(void) {
  int a, newA = -1;
  scanf("%d", &a);

  int count = 0;
  while (a != newA) {
    int first, second;
    int newFirst, newSecond;

    if (count == 0) {
      first = a / 10;
      second = a % 10;
    } else {
      first = newA / 10;
      second = newA % 10;
    }

    newFirst = second;
    newSecond = (first + second) % 10;

    newA = newFirst * 10 + newSecond;

    count++;
  }

  printf("%d", count);

  return 0;
}