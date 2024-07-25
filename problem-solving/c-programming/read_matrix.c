#include <stdio.h>

/*
A C program to read a matrix of size m x n from the keyboard and display the
same on the screen, enable your program to accept input from user.
*/
 
#define MAXROW 3
#define MAXCOL 3

int main(){
    int matrix[MAXROW][MAXCOL];

    printf("\nEnter matrix elements :\n");
    for(int i = 0; i < 3; i++){
        for(int j = 0; j < 3; j++){
            printf("Enter element of row %d column %d [%d, %d] : ",i + 1, j + 1, i + 1, j + 1);
            scanf("%d", &matrix[i][j]);
        }
        printf("\n"); // new line after row elements
    }

    printf("\nThe matrix is :\n");
    for(int i = 0; i < 3; i++){
        for(int j = 0; j < 3; j++){
            printf("  %d\t", matrix[i][j]);
        }
        printf("\n"); // new line after row elements
    }
    return 0;
}

/*
Output:

Enter matrix elements :
Enter element of row 1 column 1 [1, 1] : 12
Enter element of row 1 column 2 [1, 2] : 34
Enter element of row 1 column 3 [1, 3] : 56

Enter element of row 2 column 1 [2, 1] : 87
Enter element of row 2 column 2 [2, 2] : 90
Enter element of row 2 column 3 [2, 3] : 55

Enter element of row 3 column 1 [3, 1] : 32
Enter element of row 3 column 2 [3, 2] : 17
Enter element of row 3 column 3 [3, 3] : 23


The matrix is :
  12	34	56	
  87	90	55	
  32	17	23
*/
