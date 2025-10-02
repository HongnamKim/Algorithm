#include <stdio.h>

int main(void) {
  int N;
  scanf("%d", &N);

  float scores[N];

  for (int i = 0; i < N; i++) {
    scanf("%f", &scores[i]);
  }

  float max = scores[0];

  for (int i = 0; i < N; i++) {
    if (max < scores[i]) {
      max = scores[i];
    }
  }

  float avg = 0;

  for (int i = 0; i < N; i++) {
    scores[i] = scores[i] / max * 100;
    avg = avg + scores[i];
  }

  avg = avg / N;

  printf("%f", avg);

  return 0;
}