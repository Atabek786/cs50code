import sys
import os
import csv


def process_data(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = ['first', 'last', 'house']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            full_name = row['name']
            house = row['house']
            last, first = full_name.split(', ')
            row['first'] = first
            row['last'] = last
            row.pop('name', None)
            writer.writerow(row)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script_name.py input.csv output.csv")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    process_data(input_file, output_file)

    print(f"Data edited and saved to {output_file}")
