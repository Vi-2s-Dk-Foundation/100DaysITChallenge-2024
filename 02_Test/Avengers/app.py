# Project 
from flask import Flask, render_template, request
import random

app = Flask(__name__)

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

word = random.choice(avengers).upper()
word_display = "_ " * len(word)
guesses = set()

@app.route('/')
def index():
    return render_template('index.html', word=word, word_display=word_display)

@app.route('/guess', methods=['POST'])
def process_guess():
    user_guess = request.form['user_guess'].upper()
    word = request.form['word'].upper() 
    guesses = set(request.form['guesses']) 
    incorrect_guesses = int(request.form['incorrect_guesses'])

    if user_guess in guesses:
        message = "You already guessed that letter."
    elif user_guess not in word:
        incorrect_guesses += 1
        message = "Incorrect guess."
    else:
        message = "Good guess!"

    guesses.add(user_guess)
    word_display = ""
    for letter in word:
        if letter in guesses:
            word_display += letter + " "
        else:
            word_display += "_ "

    print(guesses)
    print(*guesses)
    if all(letter in guesses for letter in word):
        message = f"Congratulations! You guessed the Avenger: {word}"
        return render_template('result.html', message=message, won=True, word=word)

    if incorrect_guesses >= 3:  # Adjust max guesses as needed
        message = f"You have exceeded the number of guesses. The Avenger was: {word}"
        return render_template('result.html', message=message, won=False, word=word)

    return render_template('game.html', word_display=word_display, message=message, 
                           guesses=guesses, word=word, incorrect_guesses=incorrect_guesses) 

@app.route('/reset')
def reset_game():
    # Clear session data (if using sessions)
    # session.clear() 

    word = random.choice(avengers).upper()
    word_display = "_ " * len(word)
    guesses = set()
    incorrect_guesses = 0 

    return render_template('index.html', word=word, word_display=word_display, guesses=guesses, incorrect_guesses=incorrect_guesses) 

if __name__ == '__main__':
    app.run(debug=True)
