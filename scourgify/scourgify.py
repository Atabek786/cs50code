import sys
import os
import csv

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row['name']
                house = row['house']
            return name, house
    except FileNotFoundError:
        print("File not found")

def write_file(file):
    try:
        with open(file, 'w', newline='') as filewrite:
            fielnames = ['first', 'last', 'house']
            

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