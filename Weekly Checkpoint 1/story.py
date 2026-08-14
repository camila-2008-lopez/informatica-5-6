def main():
    # planet =  input("Planet: ")

    # # Separation
    # print("Hello", planet)

    # # Ending
    # print("Hello", end=" ")
    # print(planet)

    # #Concatenation
    # print("Hello " + planet)

    # # Formatted String
    # print(f"Hello {planet}")

    name = input("Whats your name? ")
    color = input("Tell me a color: ")
    adj = input("Give me an adjective: ")
    goal = input("A goal you would like to achieve: ")

    print(f"Hello{name}!")
    print()

    print("This is your story:")
    print(f"At dawn the sky turned {color}, and the air felt {adj}. I decided today I will finally{goal}.")

if __name__=="__main__":
    main()

