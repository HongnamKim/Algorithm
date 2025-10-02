#include <stdio.h>
#include <math.h>

// parameter로 전달받은 수를 자리수 확인 + 분리
// 각 자리수 별 공차가 일정한지 확인.
// 일정하면 해당 input 출력
// 일정하지 않다면 1 작은 수를 parameter로 함수 호출

int hansu(int input) {
  int done = 1;
  int returnInput;
  int order;
  int common;

  while (done){
    returnInput = input;
    order = ceil(log10f((float) input));

    if (order == 0){
      return returnInput;
    }

    int orderArr[order];

    // 자리수 분리
    for (int i = 0; i < order; i++){
      orderArr[i] = input / (int)pow(10, (order -1 - i));
      input = input % (int)pow(10, (order -1 - i));
    }
    // 공차 확인
    if (order < 3){
      return returnInput;
    }
    else{
      common = orderArr[1] - orderArr[0];
      printf("%d\n", common);
    }

    for (int i = 1; i < order-1; i++){
      if(orderArr[i+1]-orderArr[i] == common){
        printf("same");
        done = 0;
      }
      else{
        printf("different");
        done = 1;
      }
    }

    if (done == 1){
      input = returnInput - 1;
      done = 1;
    }
  }
  return returnInput;
}

int main(void) {
  int input;
  scanf("%d", &input);
  printf("%d", hansu(input));
  return 0;
}