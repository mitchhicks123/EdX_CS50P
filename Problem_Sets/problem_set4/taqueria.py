def main():
    #define menu using dictionary
  menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
  }

  cost_calculator(menu)

#function that calculates the cost of the food items
def cost_calculator(food_items):
  cost = 0
  #ask user for there order unless they ctrl z to finish order
  while True:
    try:
      user_in = input("Items: ").title().strip()

    except EOFError:
      break

    #add to the total food bill
    else:
      if user_in in food_items:
        cost = cost + food_items[user_in]
        print(f"${cost:.2f}")




#call main
main()