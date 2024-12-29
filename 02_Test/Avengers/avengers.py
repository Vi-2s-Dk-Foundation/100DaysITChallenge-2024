import random

avengers = [
    "Iron Man", "Captain America", "Thor", "Hulk", "Black Widow", "Hawkeye",
    "Spider-Man", "Doctor Strange", "Black Panther", "Scarlet Witch", 
    "Vision", "Ant-Man", "Wasp", "Falcon", "Winter Soldier", "War Machine",
    "Star-Lord", "Gamora", "Drax", "Rocket", "Groot", "Nebula", "Mantis"
]

word = random.choice(avengers).upper()
word_display = "_ " * len(word)
guesses = []

attempts = 3

while attempts > 0:

    #Print word display
    print(f"Your AVENGER is:\n {word_display}")

    # Get user to guess letter
    guess = input("Guess a letter:\n")

    # Check if letter is in word
    if guess in word:
        message = "Correct!"
        for letter in word:
            if letter.upper() == guess.upper():
                word_display += letter.upper()
            else:
                word_display += "_ "
    else:
        message = "Incorrect!"
    
    attempts -= 1
    print(f"Your guess was...{message}")
    print(f"Number of attempts left: {attempts}")

# Game Results
print(word_display)
print(f"Your AVENGER is:\n {word}")

