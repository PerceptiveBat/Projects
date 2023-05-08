import random
from words import words
import string


def get_valid_word(words):
    word = random.choice(words) #choose random word form words.py file
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()




def hangman():
    word = get_valid_word(words)
    word_letters = set(word)     #creates a set (like a list but random positions) with the letters of the word
    alphabet = set(string.ascii_uppercase)      #creates a set with the letters of the alphabet in caps
    used_letters = set()        #empty set for the used letters by the player
    lives = 6
    while len(word_letters) > 0:
        print('You have used these letters: ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '_' for letter in word]
        print('Current word: \n', word_list)

        user_letter = input('Guess a letter \n').upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('You guessed correctly!')
            else:
                lives = lives - 1
                print('Wrong guess. You have', lives, "lives remaining.")
                if lives == 0:

                    break
        elif user_letter in used_letters:
            print('You have already guessed this letter. Try again.\n')

        else:
            print('Please guess a valid character.\n')

    if lives == 0:
        print('Sorry, you lost. The word was', word)
    else:
        print('Congratulations! You guessed ', word, 'correctly!')

hangman()
