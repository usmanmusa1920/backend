#include <stdio.h>
#include <math.h>

// myFunction
void myFunction(char name[], int age) {
    printf("Hello %s, I'm %d\n", name, age);
}

// myCalculator function
int myCalculator(int x) {
    return 5 + x;
}

int main(){
    int grade;
    char name[99] = "Student Boy";
    int num = 12;

    printf("\nThe number is `%d`, the name is `%s` \n\n", num, name);

    printf("Enter student's score: ");
    scanf("%d", &grade);

    // calling `myCalculator`
    printf("Result is `%d`\n", myCalculator(3));

    // calling `mySquare`
    printf("The square is %f\n", sqrt(6));

    // calling `myFunction`
    myFunction("Jenny", 19);

    if (grade >= 70){
        
        printf("Student got A\n");
        if (grade >= 70 && grade <= 79){
            printf("Lower level\n");
        }else if(grade >= 80 && grade <= 89){
            printf("Medium level\n");
        }else{
            printf("Higher level\n");
        }

    }else if (grade >= 60 && grade <= 69){
        printf("Student got B\n");
    }else{
        printf("Student fail\n");
    }

  return 0;
}
