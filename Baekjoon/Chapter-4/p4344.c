#include <stdio.h>

int main(void){
  int testCase;
  scanf("%d", &testCase);

  float ratioArr[testCase];
  
  for(int i = 0; i < testCase; i++){
    int scores[1000];
    int students;
    float avg = 0;
    int overAvg = 0;
    float ratio;

    //학생 수 입력
    scanf("%d", &students);

    //학생 점수 입력, 총합 계산.
    for (int j = 0; j < students; j++){
      scanf("%d", &scores[j]);
      avg += scores[j];
    }
    //학생 평균 계산
    avg = avg / students;
    
    //평균 넘는 학생수 count
    for (int j = 0; j < students; j++){
      if (avg < scores[j]){
        overAvg++;
      }
    }
    
    // 평균 넘는 비율 계산
    ratio = (float)overAvg / (float)students * 100;
  
    // 비율 업데이트  
    ratioArr[i] = ratio;
  }

  for (int i = 0; i < testCase; i++){
    printf("%.3f%%\n", ratioArr[i]);
  }
  return 0;
}
  



  
