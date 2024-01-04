#include <stdio.h>

/*
C programm that print numbers from 80 to 30 using do-while loop.
*/

int main(){
    int a = 80;
    do{
        printf("%d\n", a);
        a--;
    }while(a >= 30 && a <= 80);
    return 0;
}
