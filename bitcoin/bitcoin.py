import sys, requests

url = 'https://api.coindesk.com/v1/bpi/currentprice.json'


if len(sys.argv) < 2:
    print("Missing command-line argument")
else:
    if not sys.argv[1].isdigit():
        print("Command-line argument is not a number")
    else:

