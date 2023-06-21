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

    // Calculate the number of audio samples
    long numSamples = header.subchunk2Size / (header.bitsPerSample / 8);

    // Allocate memory for audio data
    int16_t *audioData = (int16_t *)malloc(numSamples * sizeof(int16_t));

    // Read audio data
    fread(audioData, sizeof(int16_t), numSamples, input);

    // Reverse audio data
    for (long i = 0; i < numSamples / 2; i++)
    {
        int16_t temp = audioData[i];
        audioData[i] = audioData[numSamples - 1 - i];
        audioData[numSamples - 1 - i] = temp;
    }

    // Write reversed audio to file
    fwrite(audioData, sizeof(int16_t), numSamples, output);

    // Free allocated memory
    free(audioData);

    // Close files
    fclose(input);
    fclose(output);

    return 0;
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
}

int get_block_size(WAVHEADER header)
{
    // TODO #7
    int block = 0;
    block = header.numChannels * (header.bitsPerSample / 8);
    return block;
}