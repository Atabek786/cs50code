import sys
import os
import csv

def read_file(file_path):
    data = []
    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print("File not found")
    return data


def write_file(file, data):
    try:
        with open(file, 'w', newline='') as file:
            fieldnames = ['first', 'last', 'house']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
    except IOError:
        print('Error writing to file')

if __name__ == "__main__":
    if len(sys.argv)  < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)
    elif not sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv"):
        print("Not a csv file")
        sys.exit(1)
    elif not os.path.exists(sys.argv[1]):
        print("Could not read "+ sys.argv[1])
        sys.exit(1)
    else:
        input_file = sys.argv[1]
        
        # Get the output file name based on the input file name
        base_name = os.path.splitext(os.path.basename(input_file))[0]
        output_file = f"{base_name}_after.csv"

        before = read_file(input_file)
        for row in before:
            full_name = row['name']
            house = row['house']
            last, first = full_name.split(', ')
            row['first'] = first
            row['last'] = last
            row.pop('name', None)


        write_file(output_file, before)

    print(f"Data edited and saved to {output_file}")