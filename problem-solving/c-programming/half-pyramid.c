#include <stdio.h>

int main(){
  char alp[10][13] = {"1", "1 1", "1 1 1", "1 1 1 1", "1 1 1 1 1", "1 1 1 1 1 1", "1 1 1 1 1 1 1"};

  printf("1\n");
  for (int i = 1; i <= 6; i++){
    printf("%s\n", alp[i]);
  }
  return 0;
}

/*
OUTPUT:

1
1 1
1 1 1
1 1 1 1
1 1 1 1 1
1 1 1 1 1 1
1 1 1 1 1 1 1

*/