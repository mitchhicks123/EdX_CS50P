#import required libraries
import json
import requests
import sys

#main function
def main():
    #get users command line input for amount of bitcoins
    amount_btc = get_input()

    #call function that uses coindesks api to get the current price of bitcoin
    print(f"${get_btc_info() * amount_btc:,.4f}")

#this function validates users command line input
def get_input():
    #verify command line arguement is a number
    try:
        amount = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line arguement not a number")
    except IndexError:
        sys.exit("Missing Command-line arguement")

    else:
        return amount

#this function gets current price of bitcoin via coindeask api
def get_btc_info():
    btc_info = requests.get(
        "https://api.coindesk.com/v1/bpi/currentprice.json")

    return btc_info.json()["bpi"]["USD"]["rate_float"]

#call main function
main()
