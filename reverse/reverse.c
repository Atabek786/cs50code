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
    FILE *input = fopen(argv[1], "rb");
    if (input == NULL)
    {
        printf("Cannot open input file\n");
        return 1;
    }

    // Read header
    WAVHEADER header;
    fread(&header, sizeof(WAVHEADER), 1, input);

    if (!check_format(header))
    {
        printf("Invalid WAV format\n");
        fclose(input);
        return 1;
    }

    // Open output file for writing
    FILE *output = fopen(argv[2], "wb");
    if (output == NULL)
    {
        printf("Cannot open output file\n");
        fclose(input);
        return 1;
    }

    // Write header to output file
    fwrite(&header, sizeof(WAVHEADER), 1, output);

    // Get block size
    int block_size = get_block_size(header);

    // Calculate size of audio data
    fseek(input, 0, SEEK_END);
    long file_size = ftell(input);
    long audio_data_size = file_size - sizeof(WAVHEADER);

    // Calculate number of blocks in the audio data
    long num_blocks = (audio_data_size + block_size - 1) / block_size;

    // Read and write audio blocks in reverse order
    for (long i = num_blocks - 1; i >= 0; i--)
    {
        // Set input file pointer to the beginning of the current block
        fseek(input, sizeof(WAVHEADER) + i * block_size, SEEK_SET);

        // Read audio block
        uint8_t *block = malloc(block_size);
        fread(block, 1, block_size, input);

        // Write audio block to output file
        fwrite(block, 1, block_size, output);

        // Free memory
        free(block);
    }

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
    int bytes_per_sample = header.bitsPerSample / 8;
    int block_size = header.numChannels * bytes_per_sample;
    return block_size;
}
