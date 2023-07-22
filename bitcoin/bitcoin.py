import sys
import requests
import locale

url = 'https://api.coindesk.com/v1/bpi/currentprice.json'

if len(sys.argv) < 2:
    print("Missing command-line argument")
else:
    try:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            # The JSON response has a 'bpi' key that contains the price data in different currencies
            price_usd = float(data['bpi']['USD']['rate'].replace(',',''))

            inbitcoin = float(sys.argv[1]) * price_usd

            locale.setlocale(locale.LC_ALL, '')

            formated = locale.format_string("%.4f", inbitcoin, grouping=True)
            print(f"${formated}")
        else:
            print(f"Request failed with status code: {response.status_code}")
    except ValueError:
        print("Enter a number of bitcoins")

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
