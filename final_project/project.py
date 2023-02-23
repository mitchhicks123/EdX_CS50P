
from stock import Stocks
import matplotlib as mpl
import matplotlib.pyplot as plt
import yfinance as yf
from datetime import datetime
from dateutil.relativedelta import relativedelta
import sys


def main():
    # get users input this is to test some of the code
    ticker = input("Ticker: ").strip().upper()

    # create a a stock object
    stock = Stocks(ticker)
    print(stock.print_all())
    test = stock.revenue
    test.reverse()
    time_period = get_reporting_years(len(test))

    plt.bar(time_period, test)
    plt.xlabel('Revenue')
    plt.ylabel('Amount in Billions')
    plt.title('Amount over the past 5 years')
    plt.show()
    sys.exit()


def get_reporting_years(count):
    years = []
    for i in range(count, 0, -1):
        years.append((datetime.now() - relativedelta(years=i)).strftime('%Y'))
    return years


if __name__ == "__main__":
    main()
