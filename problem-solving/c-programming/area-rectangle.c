#include <stdio.h>

// calculate area of rectangle

int main(){
  float breadth;
  float length;
  float area;

  printf("Enter the breadth: ");
  scanf("%f", &breadth);

  printf("Enter the length: ");
  scanf("%f", &length);

  area = length * breadth;

  printf("The area of the rectangle is: %f\n", area);
  return 0;
}

/*
OUTPUT:

Enter the breadth: 12.5
Enter the length: 34.76
The area of the rectangle is: 434.499969
*/