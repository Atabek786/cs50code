import sys
import requests

url = 'https://api.coindesk.com/v1/bpi/currentprice.json'

if len(sys.argv) < 2:
    print("Missing command-line argument")
else:
    if not sys.argv[1].isdigit():
        print("Command-line argument is not a number")
        sys.exit()
    else:
        try:
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                # The JSON response has a 'bpi' key that contains the price data in different currencies
                price_usd = float(data['bpi']['USD']['rate'].replace(',',''))

                result = int(sys.argv[1]) * price_usd
                print(result)
            else:
                print(f"Request failed with status code: {response.status_code}")

        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")
