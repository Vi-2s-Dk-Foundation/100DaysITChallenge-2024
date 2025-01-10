import random

def get_random_word(word_list):
    """
    Selects a random word from the given list.

    Args:
        word_list (list): A list of words.

    Returns:
        str: A randomly selected word in uppercase.
    """
    return random.choice(word_list).upper()

def display_word(word, guesses):
    """
    Displays the word with guessed letters and underscores.

    Args:
        word (str): The word to be guessed.
        guesses (set): A set of guessed letters.

    Returns:
        str: The word with guessed letters revealed and unguessed letters replaced with underscores.
    """
    word_display = ""
    for letter in word:
        if letter in guesses:
            word_display += letter + " "
        else:
            word_display += "_ "
    return word_display

def get_difficulty_level(difficulty):
    """
    Determines the maximum number of guesses based on the selected difficulty.

    Args:
        difficulty (str): The selected difficulty level ("easy", "medium", or "hard").

    Returns:
        int: The maximum number of guesses for the selected difficulty.
    """
    if difficulty == "easy":
        return 10
    elif difficulty == "medium":
        return 7
    elif difficulty == "hard":
        return 5
    else:
        return 5  # Default to hard if invalid difficulty is provided

def play_game(word, max_guesses):
    """
    Manages the core game logic.

    Args:
        word (str): The word to be guessed.
        max_guesses (int): The maximum number of allowed guesses.

    Returns:
        tuple: A tuple containing the final game status (True for win, False for loss), 
               the number of remaining guesses, 
               the final word display, 
               and a list of guessed letters.
    """
    guesses = set()
    remaining_guesses = max_guesses

    while remaining_guesses > 0:
        guess = input("Guess a letter: ").upper() 
        # For Flask, get the guess from the request 
        # Replace the above line with:
        # guess = request.form.get('guess', '').upper() 

        while not guess.isalpha() or len(guess) != 1:
            # Handle invalid input in your Flask route
            pass 

        if guess in guesses:
            message = "You already guessed that letter."
        elif guess in word:
            message = f"Good guess! {guess} is in the word."
        else:
            message = f"Bad guess! {guess} is not in the word."
            remaining_guesses -= 1

        guesses.add(guess)

        word_display = display_word(word, guesses)
        # print(word_display)  # Remove this for Flask

        if all(letter in guesses for letter in word):
            message = f"Congratulations! You guessed the Avenger: {word}"
            return True, remaining_guesses, word_display, list(guesses) 

    message = f"You have exceeded the number of guesses. The Avenger was: {word}"
    return False, remaining_guesses, word_display, list(guesses)