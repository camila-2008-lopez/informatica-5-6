# Create a TXT file with all of the words.

# Define the main function

# Use with to open the TXT file

def main():
    # Read a file
    with open("hangman.txt") as file:
        content = file.read()
        print(content)

    # Turn file into a
    with open("hangman.txt") as start_game:
        (word_list) = start_game.read().splitlines()


    for game in range(start_game):
        print(f"Game {game + 1}: {word_list[game]}")
    ("hangman.txt")








if __name__== "__main__":
    main()




