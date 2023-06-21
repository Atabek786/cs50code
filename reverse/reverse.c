#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#include "wav.h"

int check_format(WAVHEADER header);
int get_block_size(WAVHEADER header);

int main(int argc, char *argv[])
{
    // Ensure proper usage
    // TODO #1
    if(argc != 3)
    {
        printf("Usage: ./reverse input.wav output.wav");
        return 1;
    }

    // Open input file for reading
    // TODO #2
    FILE *input = fopen (argv[1], "r");

    if(input == NULL)
    {
        printf("File doesn't exist");
        return 1;
    }

    // Read header
    // TODO #3
    uint8_t buffer;
    fread(&buffer, sizeof(uint8_t), 1, input);

    // Use check_format to ensure WAV format
    // TODO #4
    if (check_format(&header))
    {
        return true;
    }

    // Open output file for writing
    // TODO #5

    // Write header to file
    // TODO #6

    // Use get_block_size to calculate size of block
    // TODO #7

    // Write reversed audio to file
    // TODO #8


    // closing files
    fclose(input);
}

int check_format(WAVHEADER header)
{
    // TODO #4
    const char* filename;
    FILE *input = fopen(filename, "r");

    fread(&header, sizeof(WAVHEADER), 1, input);

    // Compare the chunk ID and format to verify if it's a WAV file
        if (memcmp(header.chunkID, "RIFF", 4) == 0 && memcmp(header.format, "WAVE", 4) == 0)
        {
            fclose(input);
            return true;
        }
        else
        {
            fclose(input);
            return false;
        }

        return 0;
}

int get_block_size(WAVHEADER header)
{
    // TODO #7
    return 0;
}