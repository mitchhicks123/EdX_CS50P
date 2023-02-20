# this file will be used as a library for final_project.py

# yfiance might seems quite unpredictable and was down check link for fix: https://github.com/ranaroussi/yfinance/issues/1407
# import yfinance as yf
import json
import requests
import api


class Stocks:
    def __init__(self, ticker):
        # try and catch ticker symbol
        self.ticker = ticker
        # overview
        self.pe, self.shares_out, self.market_cap = api.get_overview(ticker)
        self.share_price = int(self.market_cap) / int(self.shares_out)
        # income statement
        self.revenue, self.gp, self.op, self.ni = api.get_income(ticker)
        # Cash Flow Statement
        # Balance Sheet

    def print_all(self):
        return (f"{self.revenue} \n{self.gp} \n{self.op} \n{self.ni}\n-----\n{self.pe}\n{self.shares_out}\n{self.market_cap}\n{self.share_price}")
