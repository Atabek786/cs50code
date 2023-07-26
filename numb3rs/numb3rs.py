import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    # Use regex to check for a valid IPv4 address format with exactly four octets
    if check := re.search(r"^(25[0-5]|2[0-4]\d|1\d\d|\d{1,2})\.(25[0-5]|2[0-4]\d|1\d\d|\d{1,2})\.(25[0-5]|2[0-4]\d|1\d\d|\d{1,2})\.(25[0-5]|2[0-4]\d|1\d\d|\d{1,2})$", ip):
        return True
    else:
        return False


if __name__ == "__main__":
    main()