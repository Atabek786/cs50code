import sys
import os
from tabulate import tabulate


def count_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(row)
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
        sys.exit()
    else:
        result = count_lines(sys.argv[1])
        final_result = tabulate(result)
        print(f"{final_result}")