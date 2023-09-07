#include <stdio.h>

int main(){
  int a;
  int i;
  int z;

  printf("Enter value of i: ");
  scanf("%d", &i);

  // for loop
  for (i = 0; i < 12; i++){
    printf("I am for loop %d\n", i+1);
  }

  printf("Enter value of z: ");
  scanf("%d", &z);

  // while loop
  while (i == 10){
    printf("I am while loop\n");
  }

  printf("Enter value of a: ");
  scanf("%d", &a);

  // do while loop
  do{
    printf("I am do while loop\n");
    a++;
  }while(a == 10);

  // do while loop with `continue` and `break`
  do{
    if (a == 10){
      a++;
      printf("About to continue\n");
      if (a == 12){
        a++;
        printf("I will continue with loop\n");
        continue;
      }
    }
    printf("I am do while loop %d\n", a);
  }while(a == 10);
  return 0;
}
