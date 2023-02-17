# this file will be used as a library for final_project.py

# yfiance might seems quite unpredictable and was down check link for fix: https://github.com/ranaroussi/yfinance/issues/1407
# import yfinance as yf
import json
import requests


def get_data(tick, years):
    """This function will be used to get all the data from the API or module"""
    """

    url = "https://mboum-finance.p.rapidapi.com/qu/quote/income-statement"

    querystring = {"symbol": "AAPL"}

    headers = {
        "X-RapidAPI-Key": "5ad6b4dfd5msh2468f515b38baa7p197c10jsn73204c248ca8",
        "X-RapidAPI-Host": "mboum-finance.p.rapidapi.com"
    }

    response = requests.request(
        "GET", url, headers=headers, params=querystring)

    print(response.text)

    """

    overview = requests.get(
        "https://www.alphavantage.co/query?function=OVERVIEW&symbol="+tick+"&apikey=231NYPC7N5HRY91H").json()

    income = requests.get(
        "https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol="+tick+"&apikey=231NYPC7N5HRY91H").json()

    balance = requests.get(
        "https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol="+tick+"&apikey=231NYPC7N5HRY91H").json()

    cash = requests.get(
        "https://www.alphavantage.co/query?function=CASH_FLOW&symbol="+tick+"&apikey=231NYPC7N5HRY91H").json()

    return overview, income["annualReports"][years], balance["annualReports"][years], cash["annualReports"][years]
