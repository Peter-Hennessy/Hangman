import random
def hangman () :
    """
    Create random list pf words for the computer to choose from
    """

    list_of_words = ('hi', 'cat', 'home', 'country', 'computer', 'phone')
    word = random.choice(list_of_words)
    print(word)
    
     
# Welcome the Player and ask to enter their name
name = input("Please enter your name gallowman: -->")
print("Welcome", name,"Who's for hanging today!")
print("========================")
print("Try to guess in less than 5 attempts")
hangman()





# Create hangman board, guessed letters, and remaing lives
HANGMAN = ['''
   +------+
   |      |
   |      |
          |
          |
          |
    =======''', '''
   +------+
   |      |
   O      |
          |
          |
          |
    =======''', '''
   +------+
   |      |
   O      |
  /|\     |
          |
          |
   ========''', '''
   +------+
   |      |
   O      |
  /|\     |
   |      |
          |
   ========''', '''
   +------+
   |      |
   O      |
  /|\     |
   |      |
  / \     |
  =========
''']
# The computer askes the player to select a character

# If the player guesses correctly, show all matched letters and display message

# if the player guesses incorrectly, dipslay falure message and delete lives

# if the player guesses all letters,  win message will appear, and loop will stop

# If the player uses all attempte, print failure and stop looping