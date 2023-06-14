#include <cs50.h>
#include <stdio.h>
#include <string.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit);

int convert(string message);

int main(void)
{
    // TODO
    string message = get_string ("Message: ");
    printf ("%d\n", convert(message));

}

void print_bulb(int bit)
{
    if (bit == 0)
    {
        // Dark emoji
        printf("\U000026AB");
    }
    else if (bit == 1)
    {
        // Light emoji
        printf("\U0001F7E1");
    }
}

int convert(string message) {
  int dec = 0, i = 0, rem;

  while (message!=0) {
    rem = message % 10;
    n /= 10;
    dec += rem * pow(2, i);
    ++i;
  }

  return dec;
}