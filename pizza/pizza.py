import sys
import os
from tabulate import tabulate
import csv

def read_file(file_path):
    try:
        with open(file_path, 'r', ) as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
            return data
    except FileNotFoundError:
        print("File not found")

if __name__ == "__main__":
    if len(sys.argv)  < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    elif not sys.argv[1].endswith(".csv"):
        print("Not a csv file")
        sys.exit(1)
    elif not os.path.exists(sys.argv[1]):
        print("File doesn't exist")
        sys.exit(1)
    else:
        result = read_file(sys.argv[1])
        final_result = tabulate(result, headers="keys", tablefmt="grid")
        print(f"{final_result}")