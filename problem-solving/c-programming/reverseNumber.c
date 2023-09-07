#include <stdio.h>

int main() 
{
    int num, reversed;

    printf("Enter a number: ");
    scanf("%d", &num);

    reversed = 0;
    while (num > 0) {
        reversed = (reversed * 10) + (num % 10);
        num = num / 10;
    }

    printf("The reversed number is %d", reversed);

    return 0;
}
