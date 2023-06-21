#include "helpers.h"

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for(int cols = 0; cols < height; cols++)
    {
        for(int rows = 0; rows < width; rows++)
        {
            int grayscal = (image[cols][rows].rgbtRed + image[cols][rows].rgbtBlue + image[cols][rows].rgbtGreen) / 3;


            image[cols][rows].rgbtRed = grayscale;
            image[cols][rows].rgbtBlue = grayscale;
            image[cols][rows].rgbtGreen = grayscale;
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
