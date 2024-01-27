#include <stdio.h>

int main(){
  float salary[5][4];

  for(int k = 0; k < 5; k++){
    for(int j = 0; j < 4; j++){
      printf("Please enter a value: ");
      scanf("%f", &salary[k][j]);
    }
    printf("\n");
  }

  /* the below code print the inputed values */
  printf("\nThe salary is :\n");
  for(int k = 0; k < 5; k++){
    for(int j = 0; j < 4; j++){
      printf("  %f\t", salary[k][j]);
    }
    printf("\n");
  }

  // grade 4 programmer
  float average, sum = 0.0;
  for(int i = 0; i < 5; i++){
    sum += salary[3][i];
  }
  average = sum / 5;
  printf("The average pay for grade 4 programmer is: %f\n", average);

  // the payment difference for each grade level
  float difference;
  for(int i = 0; i < 5; i++){
    difference = salary[i][4] - salary[i][0];
    printf("Pay difference at grade level %d is %f\n", i, difference);
  }

  // add 2.77 to the pay of grade 3 programmers
  float pay_add, sum_add = 0.0;
  for(int i = 0; i < 5; i++){
    sum_add += salary[4][i];
  }
  pay_add = sum_add + 2.77;
  printf("The average pay for grade 3 programmer when 2.77 is added is: %f\n", pay_add);

  // subtracting 1.55 from every grade level
  float difference_g;
  for(int i = 0; i < 5; i++){
    difference_g = salary[i][4] - 2.77;
    printf("For grade level %f after subtracting 2.77, it will be:", difference_g);
  }
  
  // generating multiplication table using 2D-array
  int range = 10;
  int num = 5;
  int row;
  int col;

  row = range;

  col = 3;

  int arr[row][col];

  for (int k = 0; k < row; k++){
    arr[k][0] = num;

    arr[k][1] = k + 1;

    arr[k][2] = arr[k][1] * arr[k][0];
  }

  for (int i = 0; i < row; i++){
    printf("%d * %d = %d\n", arr[i][0], arr[i][1], arr[i][2]);
  }
  return 0;
}
