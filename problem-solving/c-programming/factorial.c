#include <stdio.h>

int main(){
  int n;
  int i = 0;
  char name[10];

  printf("Enter number: ");
  scanf("%d", &n);
  printf("%d\n", n);

  printf("Enter char: ");
  scanf("%s", name);
  printf("%s\n", name);

  int fact = 1;
  while (i < n){
    i = i + 1;
    fact = fact * i;
    printf("Factorial of %d is %d\n", i, fact);
  }
  return 0;
}

/*
OUTPUT:

Enter number: 6
6
Enter char: 23
23
Factorial of 1 is 1
Factorial of 2 is 2
Factorial of 3 is 6
Factorial of 4 is 24
Factorial of 5 is 120
Factorial of 6 is 720

*/