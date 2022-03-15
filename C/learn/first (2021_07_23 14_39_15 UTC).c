#include<stdio.h>

int main(){
    float centigrate, divide;
    divide = 1.8;

    printf("What is the Value of Celcius?:\n");
    scanf("%f", &centigrate);

    printf("This is your value in Farenheit: %f", centigrate*divide + 32);
    return 0;
}