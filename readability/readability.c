#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main(void)
{
    string text = get_string("Text: ");
    int letters = 0;
    int words = 1;
    int sentences = 0;

    for (int i = 0; i <= strlen(text); i++)
    {
        if(isalpha(text[i]))
        {
            letters++;
        }

        else if (text[i] = ' ')
        {
            words++;
        }
        else if (text[i] == '.' || text[i] =='?' || text[i] == '!')
        {
            sentences++;
        }
    }
    printf ("%s\n%i letters\n", text, letters);
}