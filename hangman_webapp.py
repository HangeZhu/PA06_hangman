"""
  website_demo shows how to use templates to generate HTML
  from data selected/generated from user-supplied information
"""

from flask import Flask, render_template, request
import hangman_app
app = Flask(__name__)

def word_so_far(answer, guesses):
    return str.join('', [x if x in guesses else '_' for x in answer])

global state
state = {'guesses':[],
         'word':"interesting",
		 'word_so_far':"",
         'guesses_left': 6,
		 'done': False}

@app.route('/')
@app.route('/main')
def main():
	return render_template('hangman.html')

@app.route('/start')
def play():
    global state
    word = hangman_app.generate_random_word()
    state['word']= word
    state['word_so_far'] = '_' * len(word)
    state['chances_left'] = 6
    state['guesses'] = []
    return render_template("start.html",state=state)



@app.route('/play',methods=['GET','POST'])


def hangman():
    global state
    if request.method == 'GET':
        return play()

    elif request.method == 'POST':
        state['guesses'] += [letter]
        if letter not in state['word']:
            state['guesses_left'] -= 1
            state['word_so_far'] = word_so_far(state['word'], state['guesses'])
        return render_template('play.html',state=state)

@app.route('/about')
def about():
    return render_template('team_profile.html')


if __name__ == '__main__':
    app.run('0.0.0.0',port=3000)
