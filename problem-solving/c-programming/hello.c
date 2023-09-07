#include <stdio.h>

int main(){

  /*
    we can compile our source code by:
      gcc hello.c

    in the above we didn't specify the compile file, because it will automatically create one called `a.out` 
  */

  /*
    Method 1: How to run C programs in Linux terminal
    In order to run a C program in Linux, you need to have a C compiler present on your systems. The most popular compiler is gcc (GNU Compiler Collection).

    You can install gcc using your distribution’s package manager. In Debian and Ubuntu-based Linux distributions, use the apt command:

    sudo apt install gcc
    Switch to directory where you have kept your C program (or provide the path) and then generate the object file by compiling the program:

    gcc -o my_program my_program.c
    Keep in mind that it is optional to provide the output object file (-o my_program). If you won’t do that, an object file named a.out will be automatically generated. But this is not good because it will be overwritten for each C program and you won’t be able to know which program the a.out object file belongs to.

    Once you have your object file generated, run it to run the C program. It is already executable. Simple use it like this:

    ./my_program
    And it will display the desired output, if your program is correct. As you can see, this is not very different from running C++ programs in Linux.

    Every time you make a change in your program, you have to compile it first and then run the generated object file to run the C program.
  */

  int a = 10;
  int b = 2;

  int c = a + b;

  printf("The sum of a and b is %d \n", c);

  return 0;
}