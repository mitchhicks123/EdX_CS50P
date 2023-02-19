# this file will be used as a library for final_project.py

# yfiance might seems quite unpredictable and was down check link for fix: https://github.com/ranaroussi/yfinance/issues/1407
# import yfinance as yf
import json
import requests


class Stock:
    def __init__(self, ticker, revenue, gross_profit, op_income, net_in, eps, shareholders_eq, cash_flow, cap_ex):
        ...


def get_rev(income):
    revenue = []
    for rev in income["annualReports"]:
        revenue.append(rev["totalRevenue"])

    return revenue


def get_gp(income):
    gp = []
    for gross_profit in income["annualReports"]:
        gp.append(gross_profit["grossProfit"])

    return gp
