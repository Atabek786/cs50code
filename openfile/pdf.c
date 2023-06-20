#include <cs50.h>
#include <stdio.h>
#include <stdint.h>

int main (int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Error!");
        return 1;
    }

    //Open file

    string filename = argv[1];
    FILE *file = fopen(filename, "r");

    //Check if file exists

    if (file == NULL)
    {
        printf("No file found.\n");
        return 1;
    }


    uint8_t buffer[4];
    fread(buffer, 1, 4, file);
    for (int i = 0; i < 4; i++)
    {
        printf("%i ", buffer[i]);
    }
    printf("\n");
}