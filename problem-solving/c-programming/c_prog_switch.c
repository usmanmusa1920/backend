#include <stdio.h>
#include <string.h>

void my(int a, char name[]){
  printf("The game is over %s\n", name);
}

int main(){
  int a, b;
  char name[30] = "My name is Usman Musa";

  printf("Enter value of a: ");
  scanf("%d", &a);

  printf("Enter name: ");
  // scanf("%s", name);
  // scanf("%[^\n]", name);
  // fgets(name, 30, stdin);
  my(a, name);

  printf("\n");
  for(int i = 0; i < strlen(name); i++){
    printf("%c", name[i]);
  }
  printf("\n\n");

  switch(a){
    case 10:
      printf("a is 10\n");
      break;
    case 20:
      printf("a is 20\n");
      break;
    case 30:
      printf("a is 30\n");
      break;
    default:
      printf("Hello world, something error\n");
  }
  return 0;
}
