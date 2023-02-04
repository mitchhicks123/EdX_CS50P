# Problem 2: Coke a Cola Machine

#main function
def main():
    amount_due = 50

    #set up while loop to ask user to insert a coin
    while True:
        #print amount owed
        print("Amount Due:", amount_due)
        #ask user for input
        coin_insert = int(input("Insert Coin: "))

        #check if the coin entered is a valid unit, if it is then subtract from amount owed
        if coin_insert == 25 or coin_insert == 10 or coin_insert == 5:
            amount_due -= coin_insert

        #check if their is change owed
        if amount_due <= 0:
            change_owed = amount_due * -1
            break

    print("Change Owed:", change_owed)

#call main
if __name__ == "__main__":
    main()
