def main():
    print("Welcome to the times table quiz")

    times_table = int(input("Enter a times table that you would like to be tested on: "))

    if 1 <= times_table <= 10:

        print(f"Here is the {times_table} times table")

        for x in range(1, 11):
            answer = 6 * times_table
            print(f"{6} times {times_table} is {answer}")
    else:
        print("Invalid command.")



    max_value = int(input())
    range()

    user_answer = int()
    




if __name__=="__main__":
    main()
