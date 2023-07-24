import sys
import os
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
    if len(sys.argv)  < 4:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 4:
        print("Too many command-line arguments")
        sys.exit(1)
    elif not sys.argv[2].endswith(".csv") and sys.argv[3].endswith(".csv"):
        print("Not a csv file")
        sys.exit(1)
    elif not os.path.exists(sys.argv[2]):
        print("File doesn't exist")
        sys.exit(1)
    else:
        ...