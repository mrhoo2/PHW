from random import randint

# Generate string code with random integers 1-9
code = f"{randint(1, 9)},{randint(1, 9)},{randint(1, 9)}"
# Allow user to guess string code
guess = input("[keypad]> ")
# Initialize number of guesses
guesses = 0

# Split code into integers to allow for comparison
code_int = [int(x) for x in code.split(",")]
for x in code_int:
    print(x)


# Compare user input to generated code, up to 10 guesses
while guesses < 10:

    # Split guess into integers to allow for comparison
    guess_int = [int(x) for x in guess]
    for x in guess_int:
        print(x)

    for x in range(0, 3):
        # Provide feedback that the guess is right
        if code_int[x] == guess_int[x]:
            print("*tick*")
        # Provide feedback that the guess is wrong
        else:
            print("B" + "Z" * abs(code_int[x] - guess_int[x]) + "D!")

    if code_int == guess_int:
        break

    # Increment number of guesses if user input is wrong
    guesses += 1
    # Allow user to guess again
    guess = input("[keypad]> ")

if guesses < 10:
    print("THe lock opens. Congrats!")
else:
    print("You have failed, and died. Whoops!")
