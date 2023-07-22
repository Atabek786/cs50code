import sys
import requests
import locale

url = 'https://api.coindesk.com/v1/bpi/currentprice.json'

def format_currency(amount):
    # Set the locale to use a comma as the thousands separator
    locale.setlocale(locale.LC_ALL, '')
    # Format the amount to two decimal places with comma as thousands separator
    return locale.format_string("%.4f", amount, grouping=True)

def get_bitcoin_price():
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            # The JSON response has a 'bpi' key that contains the price data in different currencies
            price_usd = float(data['bpi']['USD']['rate'].replace(',', ''))
            return price_usd
        else:
            print(f"Request failed with status code: {response.status_code}")
            sys.exit(1)
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        sys.exit(1)

if len(sys.argv) < 2:
    print("Missing command-line argument")
    sys.exit(1)
else:
    try:
        btc_amount = float(sys.argv[1])
    except ValueError:
        print("Invalid command-line argument. Please provide a valid number.")
        sys.exit(1)

    price_usd = get_bitcoin_price()
    in_usd = btc_amount * price_usd
    formatted_result = format_currency(in_usd)
    print(f"${formatted_result}")
