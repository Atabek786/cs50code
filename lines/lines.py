import sys


def count_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        lines_of_code = sum(1 for line in lines if line.strip() and not line.strip().startswith('#'))
    return lines_of_code

if __name__ == "__main__":
    if len(sys.argv)  < 1:
        print("Too few command-line arguments")
        sys.exit()
    elif len(sys.argv) > 1:
        print("Too many command-line arguments")
        sys.exit()
    elif sys.argv