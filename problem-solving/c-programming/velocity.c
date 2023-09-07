#include <stdio.h>

// this program will receive initial velocity(u), acceleration(a), and time(t)
// calculate and display displacement(s) using formula [S = ut + 0.5at^2]

int main(){
  float acc; // acceleration
  float time; // time
  float vel;  // velocity
  float dis;  // displacement
  float ut;  // velocity * time
  float at;  // acceleration * time
  float at_sqrt;  // at ^ 2
  float times_point_5;  // at_sqrt * 0.5

  printf("Enter velocity: ");
  scanf("%f", &vel);

  printf("Enter acceleration: ");
  scanf("%f", &acc);

  printf("Enter time: ");
  scanf("%f", &time);

  ut = vel * time;
  at = acc * time;
  at_sqrt = at * at;
  times_point_5 = at_sqrt * 0.5;

  dis = ut + times_point_5;

  printf("The displacement is: %f\n", dis);
  return 0;
}

/*
OUTPUT:

Enter velocity: 12
Enter acceleration: 8.9
Enter time: 21.79
The displacement is: 19066.097656
*/