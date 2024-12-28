# Project funstions
from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # For session management

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

@app.route('/')
def index():
    session['word'] = random.choice(avengers).upper()
    session['guesses'] = ""
    session['incorrect_guesses'] = 0
    session['max_guesses'] = 10  # Default difficulty

    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def process_guess():
    user_guess = request.form['guess'].upper()
    word = session['word']
    guesses = session['guesses']
    incorrect_guesses = session['incorrect_guesses']

    if user_guess in guesses:
        message = "You already guessed that letter."
    elif user_guess not in word:
        incorrect_guesses += 1
        message = "Incorrect guess."
    else:
        message = "Good guess!"

    session['guesses'] += user_guess
    session['incorrect_guesses'] = incorrect_guesses

    word_display = ""
    for letter in word:
        if letter in guesses:
            word_display += letter + " "
        else:
            word_display += "_ "

    if all(letter in guesses for letter in word):
        message = f"Congratulations! You guessed the Avenger: {word}"
        return render_template('result.html', message=message, won=True)

    if incorrect_guesses >= session['max_guesses']:
        message = f"You have exceeded the number of guesses. The Avenger was: {word}"
        return render_template('result.html', message=message, won=False)

    return render_template('game.html', word_display=word_display, message=message)

if __name__ == '__main__':
    app.run(debug=True)