#include "helpers.h"

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int row = 0; row < height; row++)
    {
        for (int col = 0; col < width; col++)
        {
            // Calculate grayscale value
            int grayscalef = (image[row][col].rgbtRed + image[row][col].rgbtGreen + image[row][col].rgbtBlue) / 3;

            // Assign grayscale value to each RGB component
            image[row][col].rgbtRed = grayscalef;
            image[row][col].rgbtGreen = grayscalef;
            image[row][col].rgbtBlue = grayscalef;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}
