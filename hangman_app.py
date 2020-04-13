"""
   hangman_app.py is an app for playing hangman in the terminal
   it is also used as a module in the hangman_webapp flask app
"""
import random
def generate_random_word():
    words = "dog cat mouse deer snake".split()
    picked = random.choice(words)
    return(picked)

def print_word(word, guessed_letters):
    output = []
    for x in word:
        if x in guessed_letters:
            output.append(x)
        not_in = [x for x in word if x not in guessed_letters]
        if x in not_in:
            output.append('_')
    outputt=" ".join(output)
    return(outputt)

def split(word):
    return [char for char in word]

def play_hangman():

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


if __name__ == '__main__':
    play_hangman()
