#include <stdio.h>
#include <math.h>

// a program that solve quadratic equation using formula X = -b +- √b ^ 2 - 4ac / 2a

int main(){
    int a;
    int b;
    int c;
    int b_sqrt;
    int ac;
    int a2;
    int ac4;

    float ac4_divide_a2;
    float X;
    float b_sqrt_sub_ac4_divide_a2;
    float root;

    printf("Enter value of a: ");
    scanf("%d", &a);
    printf("Enter value of b: ");
    scanf("%d", &b);
    printf("Enter value of c: ");
    scanf("%d", &c);

    ac = a * c;
    a2 = 2 * a;
    b_sqrt = b * b;
    ac4 = 4 * ac;

    ac4_divide_a2 = ac4 / a2;
    b_sqrt_sub_ac4_divide_a2 = b_sqrt - ac4_divide_a2;

    root = sqrt(b_sqrt_sub_ac4_divide_a2);
    X = -b - root;
    printf("The quadratic result is: %f\n", X);
    return 0;
}
