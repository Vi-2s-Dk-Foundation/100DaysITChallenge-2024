from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    good_input = "Vitus Dk."
    bad_input = "<script> alert('This is a cross site script!')</script>"

    ## How to catch the hacker's code:
    escaped_input = escape(bad_input)
    return f"<p>Hello, {good_input}!, Caught Input:{escaped_input}</p>"

if __name__ == "__main__":
    app.run(debug=True)