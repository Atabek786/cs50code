#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <math.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    string text = get_string("Text: ");

    float L = (float) letters / (float) words * 100;
    float S = (float) sentences / (float) words * 100;

    int index = round(0.0588 * L - 0.296 * S - 15.8);

    if (index >= 16 )
    {
        printf ("Grade 16+\n");
    }
    else if (index < 1)
    {
        printf ("Before Grade 1\n");
    }
    else
    {
        printf("Grade %i\n", index);
    }
}

int count_letters(string text)
{
    int letters = 0;
    for (int i = 0; i <= strlen(text); i++)
    {
        if(isalpha(text[i]))
        {
            letters++;
        }
    }
}
int count_words(string text)
{
    int words = 1;
    for (int i = 0; i <= strlen(text); i++)
    {
        if(text[i] == ' ')
        {
            words++;
        }
    }
}
int count_sentences(string text)
{
    int sentences = 0;
    if (text[i] == '.' || text[i] =='?' || text[i] == '!')
        {
            sentences++;
        }
}








//    int letters = 0;
//    int words = 1;
//    int sentences = 0;

//    for (int i = 0; i <= strlen(text); i++)
//    {
//        if(isalpha(text[i]))
//        {
//            letters++;
//        }

//        else if (text[i] == ' ')
//        {
//            words++;
//        }
//        else if (text[i] == '.' || text[i] =='?' || text[i] == '!')
//        {
//            sentences++;
//        }
//    }