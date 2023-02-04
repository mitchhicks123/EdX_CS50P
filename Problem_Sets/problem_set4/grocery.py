#main function
def main():

  items = grocies()

  #loop through grocery list returned from grocies function... print items in sorted order
  for food_item in sorted(items):
    print(items[food_item], food_item)


def grocies():
  grocery_list ={}
  #get users grocery input
  while True:
    try:
      item = input("").upper().strip()
    except EOFError:
      return grocery_list

    else:
      grocery_list[item] = (grocery_list[item] + 1) if (item in grocery_list) else 1

#call main function
main()