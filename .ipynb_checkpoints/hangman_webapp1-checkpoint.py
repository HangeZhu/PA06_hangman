"""
  website_demo shows how to use templates to generate HTML
  from data selected/generated from user-supplied information
"""

from flask import Flask, render_template, request
import hangman_app
app = Flask(__name__)

word = hangman_app.generate_random_word()
global state
state = {'guesses':[],
         'word':'N/A',
         'word_so_far':'',
         'chances_left': 6,
         'done':False}

def word_so_far(ans, guesses):
    return str.join('', [i if i in guesses else '-' for i in ans])

@app.route('/')
@app.route('/main')
def main():
    return render_template('hangman.html')

@app.route('/start')
def play():
    global state
    word = hangman_app.generate_random_word()
    state['word']= word
    state['word_so_far'] = '-' * len(word)
    state['chances_left'] = 6
    state['guesses'] = []
    return render_template("start.html",state=state)

@app.route('/play',methods=['GET','POST'])
def hangman():
    """ plays hangman game """
    global state
    if request.method == 'GET':
        return play()

    elif request.method == 'POST':
        letter = request.form['guess']
        state['guesses'] += [letter]
        if letter not in state['word']:
            state['chances_left'] -= 1

        state['word_so_far'] = word_so_far(state['word'], state['guesses'])
        return render_template('play.html',state=state)

@app.route('/about')
def about():
    return render_template('team_profile.html')


if __name__ == '__main__':
    app.run('0.0.0.0',port=3000)