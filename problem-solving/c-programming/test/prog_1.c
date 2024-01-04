#include <stdio.h>

/*
C program using for loop that would check the condition if it is true and print the "Hello" statement 7 times, and print one time "Hi" statement if the condition is false, the termination condition is when variable is <= 10.
*/

int main(){
    for (int i = 20; i > 0; i--){
        if (i == 18){
            printf("Hi\n");
        }else if (i == 20 || i == 19){
            continue;
        }else if (i <= 10){
            break;
        }else{
            printf("Hello\n");
        }
    }
    return 0;
}
