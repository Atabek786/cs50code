#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    // Check for command line args
    if (argc != 2)
    {
        printf("Usage: ./read infile\n");
        return 1;
    }

    // Create buffer to read into
    char buffer[7];

    // Create array to store plate numbers
    char *plates[8];

    FILE *infile = fopen(argv[1], "r");

    int idx = 0;

    while (fread(buffer, 1, 7 , infile) == 7)
    {

        char *temp = malloc(sizeof(char) * 7);

        // Replace '\n' with '\0'
        buffer[6] = '\0';

        if(temp != NULL)
        {
            strcpy(temp, buffer);
        }

        plates[idx] = temp;
        temp = NULL;

        free(temp);
        idx++;
    }

    for (int i = 0; i < 8; i++)
    {
        printf("%s\n", plates[i]);
    }
    fclose(infile);
}
