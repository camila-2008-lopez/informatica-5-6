def main():
    welcome()
    choice = int(input("Select your order: "))
    get_item(choice)

def welcome():
    menu = ["Cheeseburger", "Soda" , "Fries", "Ice Cream", "Cookie"]
    print("Welcome to the restuarant!")
    print("Here's the menu:")
    for 1 in range(len(menu)):
        print(f"{1+1}. {menu[1]}")


def get_item(order):
    kitchen = ["🍔", "🍟", "🥤", "🍦", "🍪"]
    if 1 <= order <= 5:
        print(kitchen[order - 1])
    else:
        print("Not in our menu.")

    if order == 1:
        print("🍔")
    elif order == 2:
        print("🥤")



if __name__ == "__main__":
     main()
