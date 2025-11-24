import requests

class CurrencyExchangeRatesFetcher:
    API_URL = "https://api.exchangerate-api.com/v4/latest/USD"  # Free API for exchange rates

    def main(self):
        try:
            rates = self.fetch_exchange_rates()

            if rates:
                print("Currency Exchange Rates (Base: USD):")
                for currency, value in rates.items():
                    print(f"{currency}: {value:.4f}")
            else:
                print("No rates fetched. Check API or connection.")
        except Exception as e:
            print(f"Error fetching rates: {e}")

    def fetch_exchange_rates(self):
        rates = {}

        response = requests.get(self.API_URL)
        if response.status_code != 200:
            raise Exception(f"API error: HTTP {response.status_code}")

        json_response = response.json()
        if "rates" not in json_response:
            raise Exception("Invalid API response")

        rates = json_response["rates"]

        return rates

if __name__ == '__main__':
    fetcher = CurrencyExchangeRatesFetcher()
    fetcher.main()