#include <stdio.h>

/*
C program that prints all numbers between 1 and 100 inclusive using while loop.
*/

int main(){
    int a = 101;
    while (a > 1){
        a = a - 1;
        printf("%d\n", a);
    }
    return 0;
}
