#include <stdio.h>
#include <string.h> // for strcpy function

/*
    In C programming String is a 1-D array of characters and is defined as an array of characters.
    But an array of strings in C is a two-dimensional array of character types.
    Each String is terminated with a null character (\0). It is an application of a 2d array
*/

int main(){
    int a = 0, b = 0, c = 0, i = 0;
    char names[3][7] = {"Geek", "Geeks", "Geeksfor"}; // array of string

    for (int i=0; i<10; i++){
        a = a + i;
        b = b + i;
        c = c + i;
    }
    
    printf("The sum of a = %d\nThe sum of b = %d\nThe sum of c = %d\ni = %d\n", a, b, c, i);
    for (i = 0; i <= 3; i++){
        printf("%s\n", names[i]);
    }
    
    int num[10] = {0,1,2,3,4,5,6,7,8,9}; // array of numbers
    for (i = 0; i <= 10; i++){
        printf("%d\n", num[i]);
    }

    // printf("%s\n", names); // print names[2] index 2
    return 0;
}
