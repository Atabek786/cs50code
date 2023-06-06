#include <string.h>
#include <cs50.h>
#include <stdio.h>

int main (void)
{
    string word = get_string ("Word: ");

    int word_length = strlen (word);
    for (int i = 0; i < word_length - 1; i++)
    {
        //Check if NOT alphabetical (i.e., "ba")
        if (word[i] > word[i + 1])
        {
            printf ("The words ARE NOT alphabetical\n");
            return 0;
        }
    }

    printf ("The words are alphabetical\n");
    return 0;

}