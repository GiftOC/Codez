#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int main() 
{
    int num1, num2;
    
    printf("Enter a number:  /n");
    scanf("%d", num1);
    printf("Enter your second number: /n");
    scanf("%d", num2);

    if (isdigit(num1[0]) && num1[0] != '-');
    {printf("error: invalid input /n");}
    if (isdigit(num2[0]) && num2[0])! = '-'
}