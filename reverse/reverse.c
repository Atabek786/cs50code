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
    if (argc != 3)
    {
        printf("Usage: ./reverse input.wav output.wav\n");
        return 1;
    }

    // Open input file for reading
    FILE *input = fopen(argv[1], "rb");  // Use "rb" for binary mode

    if (input == NULL)
    {
        printf("File doesn't exist\n");
        return 1;
    }

    // Read header
    WAVHEADER header;
    fread(&header, sizeof(WAVHEADER), 1, input);

    // Use check_format to ensure WAV format
    if (!check_format(header))
    {
        printf("Invalid WAV file format\n");
        fclose(input);
        return 1;
    }

    // Open output file for writing
    FILE *output = fopen(argv[2], "wb");  // Use "wb" for binary mode

    if (output == NULL)
    {
        printf("Cannot create output file\n");
        fclose(input);
        return 1;
    }

    // Write header to file
    fwrite(&header, sizeof(WAVHEADER), 1, output);

    // Calculate block size
    int block = get_block_size(header);

    // Move the input pointer to the start of audio data
    fseek(input, sizeof(WAVHEADER), SEEK_SET);

    // Seek to the end of the audio data
    fseek(input, 0, SEEK_END);

    // Calculate the number of audio blocks
    long numBlocks = ftell(input) / block;

    // Allocate memory for an audio block
    uint8_t *audioBlock = (uint8_t *)malloc(block * sizeof(uint8_t));

    // Reverse and write audio blocks
    for (long i = numBlocks - 1; i >= 0; i--)
    {
        // Move the input pointer to the beginning of the current block
        fseek(input, -block, SEEK_CUR);

        // Read the audio block
        fread(audioBlock, sizeof(uint8_t), block, input);

        // Write the audio block to the output file
        fwrite(audioBlock, sizeof(uint8_t), block, output);
    }

    // Free allocated memory
    free(audioBlock);

    // Close files
    fclose(input);
    fclose(output);

    return 0;
}

int check_format(WAVHEADER header)
{
    if (memcmp(header.chunkID, "RIFF", 4) == 0 && memcmp(header.format, "WAVE", 4) == 0)
    {
        return true;
    }
    else
    {
        return false;
    }
}

int get_block_size(WAVHEADER header)
{
    int block = header.numChannels * (header.bitsPerSample / 8);  // Divide by 8 to convert bits to bytes
    return block;
}
