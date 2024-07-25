#include <stdio.h>

/*
A C program that read the values of a, b and c and display the value of x, where
  X=a/b-c

enable your program to accept input from user
Test your program for the following values:

    a) a= 250, b= 85 c= 25
    b) a= 300 b=70 c=70
*/

int main(){
    int a;
    int b;
    int c;
    float X;
    float sub; // this will store value of `b - c`

    printf("Enter value of a: ");
    scanf("%d", &a);

    printf("Enter value of b: ");
    scanf("%d", &b);

    printf("Enter value of c: ");
    scanf("%d", &c);

    sub = b - c; // subtracting `c value` from `b value`
    X = a / sub;
    printf("The value of X is: %f\n", X);

    return 0;
}

/*
Output when a, b, c = 250, 85, 25 respectively:
  Enter value of a: 250
  Enter value of b: 85
  Enter value of c: 25
  The value of X is: 4.166667


Output when a, b, c = 300, 70, 70 respectively:
  Enter value of a: 300
  Enter value of b: 70
  Enter value of c: 70
  The value of X is: inf
*/
