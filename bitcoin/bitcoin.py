import sys
import requests
import locale

url = "https://api.coindesk.com/v1/bpi/currentprice.json"


json = {
    {
        "time": {
            "updated": "Jul 22, 2023 21:28:00 UTC",
            "updatedISO": "2023-07-22T21:28:00+00:00",
            "updateduk": "Jul 22, 2023 at 22:28 BST",
        },
        "disclaimer": "This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org",
        "chartName": "Bitcoin",
        "bpi": {
            "USD": {
                "code": "USD",
                "symbol": "&#36;",
                "rate": "29,832.0354",
                "description": "United States Dollar",
                "rate_float": 29832.0354,
            },
            "GBP": {
                "code": "GBP",
                "symbol": "&pound;",
                "rate": "24,927.4101",
                "description": "British Pound Sterling",
                "rate_float": 24927.4101,
            },
            "EUR": {
                "code": "EUR",
                "symbol": "&euro;",
                "rate": "29,060.7580",
                "description": "Euro",
                "rate_float": 29060.758,
            },
        },
    }
}


def format_currency(amount):
    # Set the locale to use a comma as the thousands separator
    locale.setlocale(locale.LC_ALL, "")
    # Format the amount to two decimal places with comma as thousands separator
    return locale.format_string("%.4f", amount, grouping=True)


def get_bitcoin_price():
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            # The JSON response has a 'bpi' key that contains the price data in different currencies
            price_usd = float(data["bpi"]["USD"]["rate"].replace(",", ""))
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
    formatted_result = format_currency(in_usd).strip()
    print(f"${formatted_result}")
