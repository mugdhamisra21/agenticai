from decimal import Decimal, ROUND_HALF_UP


def main():
    portfolio = {
        "AAPL": 5000,
        "MSFT": 4000,
        "GOOGL": 3000,
        "AMZN": 2500,
        "NVDA": 6000,
        "META": 2000,
        "TSLA": 1500,
        "UNH": 1000,
        "JNJ": 2000,
        "V": 1500,
        "PG": 3000,
        "HD": 1000,
        "MA": 1200,
        "JPM": 1800,
        "AVGO": 800,
        "XOM": 2500,
        "CVX": 2000,
        "PFE": 5000,
        "ABBV": 2200
    }

    prices = {
        "AAPL": "277.55",
        "MSFT": "485.50",
        "GOOGL": "319.95",
        "AMZN": "229.16",
        "NVDA": "180.26",
        "META": "633.61",
        "TSLA": "426.58",
        "UNH": "329.71",
        "JNJ": "207.56",
        "V": "333.79",
        "PG": "148.25",
        "HD": "355.47",
        "MA": "544.93",
        "JPM": "307.64",
        "AVGO": "397.57",
        "XOM": "114.77",
        "CVX": "149.51",
        "PFE": "25.71",
        "ABBV": "227.66"
    }

    totalNAV = Decimal(0)
    scale = 2

    for ticker, shares in portfolio.items():
        price_str = prices.get(ticker)
        if price_str is not None:
            price = Decimal(price_str)
            value = price * Decimal(shares)
            totalNAV += value

    totalNAV = totalNAV.quantize(Decimal(10) ** -scale, rounding=ROUND_HALF_UP)

    print(f"NAV for today is : ${totalNAV}")


if __name__ == "__main__":
    main()