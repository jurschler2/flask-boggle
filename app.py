from boggle import Boggle
from flask import Flask, request, flash, render_template, redirect, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = 'animal crossing'

debug = DebugToolbarExtension(app)

boggle_game = Boggle()


@app.route('/')
def display_board():
    """ Creates a new game board, saves it in the session, sends to HTML
    """
    session['board'] = boggle_game.make_board()
    return render_template('base.html', board=session['board'])


@app.route('/check-word')
def check_word():
    """ Checks if the word is in the dictionary"""

    word = request.args["wordInput"]

    response = boggle_game.check_valid_word(session['board'], word)

    return jsonify(result=response)
