import requests

API_URL = "https://api.exchangerate-api.com/v4/latest/USD"  # Free API for exchange rates


def fetch_exchange_rates():
    rates = {}
    response = requests.get(API_URL)
    if response.status_code != 200:
        raise Exception(f"API error: HTTP {response.status_code}")

    json_response = response.json()
    if "rates" in json_response:
        rates = json_response["rates"]
    else:
        raise Exception("Invalid API response")

    return rates


def main():
    try:
        rates = fetch_exchange_rates()
        if rates:
            print("Currency Exchange Rates (Base: USD):")
            for currency, value in rates.items():
                print(f"{currency}: {value:.4f}")
        else:
            print("No rates fetched. Check API or connection.")
    except Exception as e:
        print(f"Error fetching rates: {e}")


if __name__ == '__main__':
    main()