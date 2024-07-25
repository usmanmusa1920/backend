#include <stdio.h>
#include <math.h>

int main (){
  
    double amount;
    double principal = 1000;
    double rate = 0.05;

    /*
        in other to run this program we have to include `-lm` flag whicg link the programm with
        the library `math.h` so that the calls to functions like pow() are resolved. like:
            gcc -o for for_loop.c -lm
    */

    for (int year = 1; year <= 10; year ++){
        amount = principal * pow (1 + rate, year);
    }

    printf("Amount = %f", amount);
    return 0;
}
