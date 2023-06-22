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
        if(n == NULL)
        {
            printf("Null here\n");
            return 1;
        }

        n->phrase = phrase;
        n->next = list;

        list = n;

        visualize(list);
    }

    unload(list);
}

void unload(node *list)
{
    while (list !=NULL)
    {
    node *ptr = list->next;
    free(list);
    list = ptr;
    }
}

void visualize(node *list)
{
    printf("<------Visualizer------>\n");
    while (list != NULL)
    {
        printf("Location %p\n", list);
        printf("Phrase: %p\n", list);
        printf("Next: %p\n", list);
    }
}