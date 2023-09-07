#include <stdio.h>

// this program will test to see if a triangle is valid or not
// by using the value entered in the keyboard

int main(){
  float angle_a;
  float angle_b;
  float angle_c;
  float sum;

  printf("Enter value for angle a: ");
  scanf("%f", &angle_a);

  printf("Enter value for angle b: ");
  scanf("%f", &angle_b);

  printf("Enter value for angle c: ");
  scanf("%f", &angle_c);

  sum = angle_a + angle_b + angle_c;

  if (sum == 180){
    printf("The triangle is valid\n");
  }else{
    printf("The triangle is in-valid\n");
  }

  return 0;
}

/*OUTPUT 1

Enter value for angle a: 12.4
Enter value for angle b: 34
Enter value for angle c: 234
The triangle is in-valid

OUTPUT 2

Enter value for angle a: 65.3
Enter value for angle b: 70.5
Enter value for angle c: 44.2
The triangle is valid
*/