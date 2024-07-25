#include <stdio.h>

// What will be the output of the following program?

int main(){
    for (int i = 0; i < 10; i++){
        printf("%d\n", i++);
        i =++ i;
    }
    return 0;
}

/*
This will give out:

0
3
6
9

*/
