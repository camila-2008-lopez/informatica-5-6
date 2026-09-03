import random
def main():
    name = input("Hello! What is your name?")
    print(f"Well, {name}, I am thinking of a number between 100.")

    # Start yhe game with random number
     number = random,randint(1, 100)
     guess = 0

    while guess != number:
       guess = int(input("Take a guess: "))
       if guess > number:
          print("Your guess is too high.")
       elif guess < number:
          print("Your guesss is to low.")


if __name__ == "__main__":
    main()

