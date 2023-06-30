# Simulate a sports tournament

import csv
import sys
import random

# Number of simluations to run
N = 1000


def main():

    # Ensure correct usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python tournament.py FILENAME")

    teams = []
    #todo: How to read teams into memory from file
    with open ('2018m.csv') as fileObject:
        # Create reader object by passing the file
        # object to reader method
        reader_obj = csv.reader(file_obj)
        # Iterate over each row in the csv
        # File using reader object
        for row in reader_obj:
            print(row)

    with open ('2019w.csv') as fileObject:
        reader_obj = csv.reader(file_obj)
        for row in reader_obj:
            print(row)

    counts = {}
    # TODO: Simulate N tournaments and keep track of win counts

    # Print each team's chances of winning, according to simulation
    for team in sorted(counts, key=lambda team: counts[team], reverse=True):
        print(f"{team}: {counts[team] * 100 / N:.1f}% chance of winning")


def simulate_game(team1, team2):
    """Simulate a game. Return True if team1 wins, False otherwise."""
    rating1 = team1["rating"]
    rating2 = team2["rating"]
    probability = 1 / (1 + 10 ** ((rating2 - rating1) / 600))
    return random.random() < probability


def simulate_round(teams):
    """Simulate a round. Return a list of winning teams."""
    winners = []

    # Simulate games for all pairs of teams
    for i in range(0, len(teams), 2):
        if simulate_game(teams[i], teams[i + 1]):
            winners.append(teams[i])
        else:
            winners.append(teams[i + 1])

    return winners


def simulate_tournament(teams):
    """Simulate a tournament. Return name of winning team."""
    # TODO


if __name__ == "__main__":
    main()
