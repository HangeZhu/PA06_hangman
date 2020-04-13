"""
  website_demo shows how to use templates to generate HTML
  from data selected/generated from user-supplied information
"""

from flask import Flask, render_template, request
import hangman_app
app = Flask(__name__)


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
	""" plays hangman game """
	global state
	if request.method == 'GET':
		return play()

	elif request.method == 'POST':

		want_to_play = input("Would you like to play again? y/n")
        while (want_to_play == 'y'):
            guessed_letters = []
            guesses_left = 6
            word = generate_random_word()
            print(print_word(word, guessed_letters))
            done = False
            while done == False:
                letter = input("Please select one letter").lower()
                if letter in guessed_letters:
                    guesses_left -= 1
                    print("You have already guessed the letter " + letter)
                elif letter not in word:
                    guessed_letters.append(letter)
                    print("The letter " + letter + " is not in the word.")
                    guesses_left -= 1
                    print(print_word(word, guessed_letters))
                else:
                    guessed_letters.append(letter)
                    print("Yes! It is in the word.")
                    print(print_word(word, guessed_letters))

                if(all(x in set(split(guessed_letters)) for x in set(split(word)))):
                    print("Congratulations! You win!")
                    done = True
                elif guesses_left == 0:
                    done = True
                    print("Sorry, your attempts have run out...")
            want_to_play = input("Would you like to play again? y/n")

		return render_template('play.html',state=state)




if __name__ == '__main__':
    app.run('0.0.0.0',port=3000)
