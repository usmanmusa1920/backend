#include <stdio.h>

// What will be the output of the following program?

int main(){
    const MAX = 10;
    int i = 1;
    for (; i < MAX; i = i/i){
        printf("%d\n", i);
    }
    return 0;
}

/*This will give us error*/
