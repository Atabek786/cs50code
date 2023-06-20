#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// preferences[i][j] is number of voters who prefer i over j
int preferences[MAX][MAX];

// locked[i][j] means i is locked in over j
bool locked[MAX][MAX];

// Each pair has a winner, loser
typedef struct
{
    int winner;
    int loser;
}
pair;

// Array of candidates
string candidates[MAX];
pair pairs[MAX * (MAX - 1) / 2];

int pair_count;
int candidate_count;

// Function prototypes
bool vote(int rank, string name, int ranks[]);
void record_preferences(int ranks[]);
void add_pairs(void);
void sort_pairs(void);
void lock_pairs(void);
void print_winner(void);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: tideman [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i] = argv[i + 1];
    }

    // Clear graph of locked in pairs
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            locked[i][j] = false;
        }
    }

    pair_count = 0;
    int voter_count = get_int("Number of voters: ");

    // Query for votes
    for (int i = 0; i < voter_count; i++)
    {
        // ranks[i] is voter's ith preference
        int ranks[candidate_count];

        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            string name = get_string("Rank %i: ", j + 1);

            if (!vote(j, name, ranks))
            {
                printf("Invalid vote.\n");
                return 3;
            }
        }

        record_preferences(ranks);

        printf("\n");
    }

    add_pairs();
    sort_pairs();
    lock_pairs();
    print_winner();
    return 0;
}

// Update ranks given a new vote
bool vote(int rank, string name, int ranks[])
{
    int j;
    j = atoi(name);
    for (int i = 0; i < candidate_count; i++)
    {
        if(strcmp(name, candidates[i])==0)
        {
            ranks[rank] = i;
            preferences[rank][i]++;

            return true;
        }
    }
    return false;
}

// Update preferences given one voter's ranks
void record_preferences(int ranks[])
{
    for (int i = 0; i < candidate_count - 1; i++)
    {
        for (int j = i + 1; j < candidate_count; j++)
        {
            int preferred_candidate = ranks[i];
            int other_candidate = ranks[j];
            preferences[preferred_candidate][other_candidate]++;
        }
    }
    return;
}

// Record pairs of candidates where one is preferred over the other
void add_pairs(void)
{
    pair_count = 0;
    for(int i = 0; i < candidate_count; i++ )
    {
        for(int j = 0; j < candidate_count; j++)
        {
            if(preferences[i][j] > preferences[j][i])
            {
                if(pair_count < MAX)
                {
                    pair new_pair;
                    new_pair.winner = i;
                    new_pair.loser = j;
                    pairs[pair_count] = new_pair;
                    pair_count++;
                }
            }
        }
    }

    return;
}

// Sort pairs in decreasing order by strength of victory
void sort_pairs(void)
{
    for(int i = 0; i < MAX - 1; i++)
    {
        for(int j = 0; j < MAX - i - 1; j++)
        {

            int strength_j = preferences[pairs[j].winner][pairs[j].loser];
            int strength_j_plus_1 = preferences[pairs[j + 1].winner][pairs[j + 1].loser];

            if(strength_j > strength_j_plus_1)
            {
                struct pair tmp = pairs[j];
                pairs[j] = pairs[j+1];
                pairs[j+1] = tmp;
            }
        }
    }
    return;
}

// Lock pairs into the candidate graph in order, without creating cycles
void lock_pairs(void)
{
    // TODO
    return;
}

// Print the winner of the election
void print_winner(void)
{
    // TODO
    return;
}