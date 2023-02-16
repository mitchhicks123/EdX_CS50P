import values
import yfinance as yf


def main():
    # get users input
    ticker = input("Ticker: ").strip().upper()
    years = int(input("Number of Years: ").strip())

    # pass values in to get data
    # values.get_data()

    company_info = values.get_data(ticker, years)
    print(company_info)
    """
    aapl = yf.Ticker("AAPL")
    print(aapl.income_stmt)
    """


if __name__ == "__main__":
    main()
