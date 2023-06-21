#include "helpers.h"
#include <math.h>
#include <string.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int row = 0; row < height; row++)
    {
        for (int col = 0; col < width; col++)
        {
            // Calculate grayscale value
            int grayscale = round((image[row][col].rgbtRed + image[row][col].rgbtGreen + image[row][col].rgbtBlue) / 3.0);

            // Assign grayscale value to each RGB component
            image[row][col].rgbtRed = grayscale;
            image[row][col].rgbtGreen = grayscale;
            image[row][col].rgbtBlue = grayscale;
        }
    }
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int row = 0; row < height; row++)
    {
        for (int col = 0; col < width; col++)
        {
            // Convert to sepia
            int sepiaRed = round(0.393 * image[row][col].rgbtRed + 0.769 * image[row][col].rgbtGreen + 0.189 * image[row][col].rgbtBlue);
            int sepiaGreen = round(0.349 * image[row][col].rgbtRed + 0.686 * image[row][col].rgbtGreen + 0.168 * image[row][col].rgbtBlue);
            int sepiaBlue = round(0.272 * image[row][col].rgbtRed + 0.534 * image[row][col].rgbtGreen + 0.131 * image[row][col].rgbtBlue);

            // Cap values at 255 if they exceed it
            image[row][col].rgbtRed = (sepiaRed > 255) ? 255 : sepiaRed;
            image[row][col].rgbtGreen = (sepiaGreen > 255) ? 255 : sepiaGreen;
            image[row][col].rgbtBlue = (sepiaBlue > 255) ? 255 : sepiaBlue;
        }
    }
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int row = 0; row < height; row++)
    {
        for (int col = 0; col < width / 2; col++)
        {
            // Swap pixels horizontally
            RGBTRIPLE temp = image[row][col];
            image[row][col] = image[row][width - col - 1];
            image[row][width - col - 1] = temp;
        }
    }
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy[height][width];
    memcpy(copy, image, sizeof(RGBTRIPLE) * height * width);

    for (int row = 0; row < height; row++)
    {
        for (int col = 0; col < width; col++)
        {
            int sumRed = 0;
            int sumGreen = 0;
            int sumBlue = 0;
            int count = 0;

            // Compute the sum of RGB values in the neighborhood
            for (int i = -1; i <= 1; i++)
            {
                for (int j = -1; j <= 1; j++)
                {
                    int newRow = row + i;
                    int newCol = col + j;

                    // Skip if out of bounds
                    if (newRow < 0 || newRow >= height || newCol < 0 || newCol >= width)
                    {
                        continue;
                    }

                    sumRed += copy[newRow][newCol].rgbtRed;
                    sumGreen += copy[newRow][newCol].rgbtGreen;
                    sumBlue += copy[newRow][newCol].rgbtBlue;
                    count++;
                }
            }

            // Assign the average of the neighborhood to the current pixel
            image[row][col].rgbtRed = round((float)sumRed / count);
            image[row][col].rgbtGreen = round((float)sumGreen / count);
            image[row][col].rgbtBlue = round((float)sumBlue / count);
        }
    }
}