#include<stdio.h>

int main(){
    float principal, time, rate_of_interest;

    printf("What is your principal amount?\n");
    scanf("%f",&principal);

    printf("What is your rate of interest(in decimal like(0.01 for 1 percent))?\n");
    scanf("%f",&rate_of_interest);

    printf("What is your Time(in years)?\n");
    scanf("%f",&time);

    float si;
    si = principal*time*rate_of_interest;

    printf("This is your simple interest:-\n%f",si);
    return 0;
}
