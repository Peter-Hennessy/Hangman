'#  Create a game of  where the player choose letters to solve a random name'
import random
import string
from words import words


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or '' in word:
        word = random.choice(words)

    return word


def hangman():
    #  letters used in the word and letters guessed
    word = get_valid_word(words)
    word_letters = set(word)  
    alphabet = set(string.ascii_uppercase)
    used_letters = set() 

    #  getting user input
    while len(word_letters) > 0:
        #  ''.join(['a', 'b', 'cd'])--> 'a b cd'
        print("you have used these letters: ", ' '.join(used_letters))

        #  what the current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("current word: ", ''.join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

        elif user_letter in used_letters:
            print("you've already guessed that one")
        else:
            print("invalid character, pleae try again")

hangman()

user_input = input("Type something:")
print(user_input)


