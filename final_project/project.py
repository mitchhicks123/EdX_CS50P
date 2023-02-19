import api
from stock import Stock
import yfinance as yf


def main():
    # get users input this is to test some of the code
    ticker = input("Ticker: ").strip().upper()

    # pass values in to get data
    # values.get_data()

    company_info = api.get_data(ticker)
    Stock()
    print(company_info)


if __name__ == "__main__":
    main()
