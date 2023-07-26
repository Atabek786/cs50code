import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    pattern = re.escape("um")
    match = re.findall(pattern, s, re.IGNORECASE)

    if match:
        return len(match)
    else:
        return None

if __name__ == "__main__":
    main()