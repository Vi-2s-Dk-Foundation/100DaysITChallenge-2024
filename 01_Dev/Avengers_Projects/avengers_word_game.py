import random # Standard built-in Python module

# Define list of Avengers words/actors
avengers = [
    "Iron Man",
    "Captain America",
    "Thor",
    "Hulk",
    "Black Widow",
    "Hawkeye",
    "Scarlet Witch",
    "Vision",
    "Spider-Man",
    "Doctor Strange",
    "Black Panther",
    "Captain Marvel",
    "Ant-Man",
    "Wasp",
    "War Machine",
    "Falcon",
    "Winter Soldier",
    "Quicksilver",
    "Groot",
    "Rocket Raccoon",
    "Guardians of the Galaxy" 
]

# Choose a random word from list
word = random.choice(avengers).upper()

# Record guesses and number of guesses
guesses = ""
guess_number = 0
good_guess = 0
bad_guess = 0

# Game info
GAME_INTRO = f"WELCOME to Avengers Word Game! \nGuess the AVENGER!!! "
word_length = len(word)

# Game screen
print(f"#" * 10) # Print hashtag 10 times
print(GAME_INTRO)

# Choose difficulty level??? 
# 28 letters in alphabet + space
# 10 guesses = easy
# 5 guesses = hard
# 3 guesses = Nick Fury

print(f"_ "* word_length) 

# Loop through the game
still_playing = True
while still_playing:
    guess = input("Guess a letter:\n").upper() # Convert input to uppercase
    guesses += guess
    guess_number += 1
    
    # Check is guess is good or bad
    if guess not in word:
        print("Incorrect guess.")
        bad_guess += 1
        print(f"Wrong Guesses: {bad_guess} ")

    else:
        print("GOOD guess!")
        good_guess += 1

    # Display the AVENGER word
    word_display = ""
    for letter in word:
        if letter in guesses:
            word_display += letter + " "
        else:
            word_display += "_ "
    print(word_display)

    # Check if all letters are guessed
    if all(letter in guesses for letter in word):
        print(f"Congratulations! You guessed the Avenger: {word}")
        print(f"# of Wrong Guesses: {bad_guess} ")
        if bad_guess == 0:
            print("FLAWLESS VICTORY!!!")
        break

    if bad_guess >=5:
        print("You have 5 Wrong Guesses!!!")
        still_playing = False
