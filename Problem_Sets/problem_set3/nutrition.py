# Problem 5: Nutrition Facts

#main function
def main():
    #take input from the user
    user_input = input("Item: ").strip().title()

    #define a list of food items
    food_items = {
        "Apple": 130,
        "Avocado": 50,
        "Banana": 110,
        "Cantaloupe": 50,
        "Grapefruit": 60,
        "Grapes": 90,
        "Honeydew Melon": 50,
        "Kiwifruit": 90,
        "Lemon": 15,
        "Lime": 20,
        "Nectarine": 60,
        "Orange": 80,
        "Peach": 60,
        "Pear": 100,
        "Pineapple": 50,
        "Plums": 70,
        "Strawberries": 50,
        "Sweet Cherries": 100,
        "Tangerine": 50,
        "Watermelon": 80
    }

    # check to see if users input is in food items
    if user_input in food_items:
        print("Calories: ", food_items[user_input])

#call main function
main()
