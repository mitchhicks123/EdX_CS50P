
from stock import Stocks
import yfinance as yf


def main():
    # get users input this is to test some of the code
    ticker = input("Ticker: ").strip().upper()

    # pass values in to get data
    stock = Stocks(ticker)
    print(stock.print_all())


if __name__ == "__main__":
    main()
