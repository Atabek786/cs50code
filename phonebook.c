#include <cs50.h>
#include <stdio.h>

int main(void)
{
    //Ask user for name, age and phone number

    char name;

    printf("Enter your name: ");

    int age;
    printf("Enter your age: ");

    char email;

    printf("Enter your email: ");

    printf("Your name is %c", name);
    printf("Your age  is %i", age);
    printf("Your email is %c", email);

    return 0;
}