#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("./caesar key\n");
        return 1;
    }

    for (int i = 0; i<strlen(argv[1]);i++)
    {
        if (!isdigit(argv[1]))
        {
            printf("./caesar key\n");
        }
        int k = atoi(argv[1]); //atoi function makes string into an integer. in the stdlib.h library

        string plaintext = get_string("Plaintext: ");
        printf("Ciphertext: ");

        for(int j = 0; j < strlen(plaintext); j++)
        {
            printf(("%c", plaintext[j] - 65 + k) % 26 + 65);
        }


    }


}