#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int maint(int argc, char *argv[])
{
    if(argc !=2)
    {
        printf("Wrong usage: Try ./create [filename]\n");
        return 1;
    }
    int filename_length = strlen(argv[1]);

    char *filename = malloc(sizeof(char) * filename_length)

    
}