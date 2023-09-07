#include <stdio.h>

// this program perfoem arithmetic operations using switch statement

int main(){
  int a;
  int b;

  printf("Enter a number: ");
  scanf("%d", &a);

  b = a * 2;

  switch(b){
    case 10:
      printf("b is equal to 10\n");
      break;
    case 20:
      printf("b is equal to 20\n");
      break;
    case 30:
      printf("b is equal to 30\n");
      break;
    default:
      printf("b is neither equal to 10, 20, and 30\n");
  }
  return 0;
}

/*
OUTPUT:

Enter a number: 10
b is equal to 20

*/