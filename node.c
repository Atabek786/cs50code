#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <cs50.h>

typedef struct node
{
    string phrase;
    struct node *next;
}
node;

#define LIST_SIZE 2

void unload(node *list);
void visualize(node *list);

int main(void)
{
    node *list = NULL;

    for(int i = 0; i < LIST_SIZE; i++)
    {
        string phrase = get_string("Enter message: ");

        node *n = malloc(sizeof(node));

        n->phrase = phrase;
        n->next = list;

        list = n;

        visualize(list);
    }

    unload(list);
}
