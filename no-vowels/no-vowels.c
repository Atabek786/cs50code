// Write a function to replace vowels with numbers
// Get practice with strings
// Get practice with command line
// Get practice with switch

#include <cs50.h>
#include <ctype.h>
#include <string.h>
#include <stdio.h>

string replace(string input);

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf ("error");
        return 1;
    }

    string word = argv [1];

    string result = replace (word);

}

string replace(string input)
{
  string output = input;

  for(int i = 0; i < strlen(input); i++)
  {
    char c = tolower(input[i]);
    printf("%c\n", input[i] );
  }
  return output;
}
