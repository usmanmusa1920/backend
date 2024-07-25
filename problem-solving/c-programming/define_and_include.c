// #include <stdio.h>
// #define name "FUGUSAU"

int main(){
    #include <stdio.h>
    // #define name "FUGUSAU"

    /*
        this program will print a constant variable if it is available else it will print `no constant variable available`

        also the `#define` can be at the top or inside the main function
    */
    char boy[10];
    printf("What is the boy's name: ");
    scanf("%s", boy);

    printf("Boy's name is `%s`\n", boy);
    char age = 10;

    //  printf("What is the moment now!? ");
    //  char moment = getchar();
    //  printf("%d", moment);
    /*the getchar() is used to take input like scanf*/

    if(age){
        printf("Yes there is age\n");
    }else{
        printf("There is no age\n");
    }
    
    #ifdef name
        printf("The constant name defined is `%s` \n", name);

    #else
        printf("No constant name defined \n");
        
    #endif
    return 0;
}
