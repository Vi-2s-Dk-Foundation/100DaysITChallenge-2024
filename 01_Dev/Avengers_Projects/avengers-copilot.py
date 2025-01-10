import random

avengers = [
    "Iron Man", "Captain America", "Thor", "Hulk", "Black Widow", "Hawkeye",
    "Spider-Man", "Doctor Strange", "Black Panther", "Scarlet Witch", 
    "Vision", "Ant-Man", "Wasp", "Falcon", "Winter Soldier", "War Machine",
    "Star-Lord", "Gamora", "Drax", "Rocket", "Groot", "Nebula", "Mantis"
]
chosen_avenger = random.choice(avengers)

print("Guess the Avenger")
hidden_word = ' '.join('_' if char != ' ' else ' ' for char in chosen_avenger)
print(hidden_word)
attempts = int(input("Enter the number of letters you want to guess: "))
guessed_letters = []

while attempts > 0:
    guess = input("Guess a letter: ").strip()
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabetic character.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)
    attempts -= 1

    display_word = ' '.join(char if char in guessed_letters or char == ' ' else '_' for char in chosen_avenger)
    print(display_word)

    if '_' not in display_word:
        print("Congratulations! You've guessed the word.")
        break
else:
    print(f"Out of attempts! The word was: {chosen_avenger}")
    while True:
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again not in ['yes', 'no']:
            print("Invalid input. Please enter 'yes' or 'no'.")
            continue
        if play_again == 'no':
            break

        chosen_avenger = random.choice(avengers)
        hidden_word = ' '.join('_' if char != ' ' else ' ' for char in chosen_avenger)
        print(hidden_word)
        while True:
            try:
                attempts = int(input("Enter the number of letters you want to guess: "))
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        guessed_letters = []

        while attempts > 0:
            guess = input("Guess a letter: ").strip().lower()
            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a single alphabetic character.")
                continue

            if guess in guessed_letters:
                print("You already guessed that letter.")
                continue

            guessed_letters.append(guess)
            attempts -= 1

            display_word = ' '.join(char if char.lower() in guessed_letters or char == ' ' else '_' for char in chosen_avenger)
            print(display_word)

            if '_' not in display_word:
                print("Congratulations! You've guessed the word.")
                break
        else:
            print(f"Out of attempts! The word was: {chosen_avenger}")
            attempts = max(1, int(len(chosen_avenger) * (1/3)))
            print(f"Guessed letters so far: {', '.join(guessed_letters)}")
            print(f"Remaining attempts: {attempts}")
            print(f"Guessed letters so far: {', '.join(guessed_letters)}")
            print(f"Remaining attempts: {attempts}")