import sys, requests



if len(sys.argv) < 2:
    print("Missing command-line argument")
else:
    if not sys.argv[1].isdigit():
        print("Command-line argument is not a number")
    else:

