import sys
import os


def count_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            lines_of_code = sum(1 for line in lines if line.strip() and not line.strip().startswith('#'))
        return lines_of_code
    except FileNotFoundError:
        print("File not found")

if __name__ == "__main__":
    if len(sys.argv)  < 1:
        print("Too few command-line arguments")
        sys.exit()
    elif len(sys.argv) > 1:
        print("Too many command-line arguments")
        sys.exit()
    elif not sys.argv[1].endswith(".py"):
        print("Not a python file")
        sys.exit()
    elif not os.path.exists(sys.argv[1]):
        print("File doesn't exist")
        sys.exit()
    else:
        result = count_lines(sys.argv[1])
        print(f"Lines of code: {result}")