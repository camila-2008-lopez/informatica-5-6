import random
def main():
    guess = int(input("Heads or tails? (press 1 for heads and 2 for tails): "))
    coin = random.randint(1, 2)

    if coin == 1:
        coin_side = "Heads"
    else:
        coin_side = "Tails"

    print(coin_side)

    if guess == coin:
        print("Winner")
    elif guess > 2:
        print("Invalid option.")
    else:
        print("Loser")



if __name__ == "__main__":
    main()
