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
        printf("Usage: ./reverse input.wav output.wav \n");
        return 0;
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
    WAVHEADER header;
    fread(&header, sizeof(WAVHEADER), 1, input);
    fclose(input);

    if (check_format(header))
    {
        return true;
    }
    else
    {
        return false;
    }

    // Open output file for writing
    // TODO #5
    FILE *output = fopen (argv[2], "w");

    if(output == NULL)
    {
        printf("File doesn't exist\n");
        return 1;
    }
    // Write header to file
    // TODO #6
    fwrite(&buffer, sizeof(uint8_t), 1, output);
    fclose(output);

    // Use get_block_size to calculate size of block
    // TODO #7
    get_block_size(header);

    // Write reversed audio to file
    // TODO #8
    int16_t buffer2;
    while(fread(&buffer2, sizeof(int16_t), 1, input))
    {
        fseek(input,)
        fwrite(&buffer, sizeof(int16_t), 1, output);
    }

    // closing files
    fclose(input);
    fclose(output);
}

int check_format(WAVHEADER header)
{
    // TODO #4
    if (memcmp(header.chunkID, "RIFF", 4) == 0 && memcmp(header.format, "WAVE", 4) == 0)
    {
        return true;
    }
    else
    {
        return false;
    }
        return 0;
}

int get_block_size(WAVHEADER header)
{
    // TODO #7
    int block = 0;
    block = header.numChannels * (header.bitsPerSample * 8);
    return 0;
}