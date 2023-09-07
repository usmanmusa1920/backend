#include <stdio.h>

//a program that calculate the product of odd numbers from 1 to 325 using a while loop.

int main(){
  int n;
  int i = 0;
  unsigned long long int r = 1;

  while (i <= 325){
    i = i + 1;
    if (i % 2 == 1){
      r = r * i;
    printf("The r at this moment is %lld, i is %d\n", r, i);
    }
  }
  i = i - 1;
  printf("\tResult (r): %lld, Result (i): %d\n", r, i);
  // unsigned long long int c;
  // c = 1LLU * 864408687 * 23;
  // printf("%lld", c);
  return 0;
}
