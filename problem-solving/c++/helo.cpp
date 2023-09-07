#include <iostream>
using namespace std;

int main(){
  int a = 10;
  string name;
  // char name[6];

  cout <<"Hello world\n";
  // cout <<"Enter number: ";
  // scanf("%d", &a);

  // cin >>name;
  cout <<"Enter name: ";
  getline(cin, name);
  // printf("Hi %s\n", name);
  printf("Number is %d\n", a);
  cout <<"The name is: " <<name <<"\n";
  return 0;
}
