import random
def hangman () :
       
    list_of_words = ['hi', 'cat', 'home', 'country', 'computer', 'phone']
    word = random.choice(list_of_words)
    attempts = 5
    guessmade = ''
    valid_entry = set ('abcdefghijklmnopqrstuvwxyz')

while len(word) > 0:
        main_word = ""
        missed = 0
 
      
for letter in word:
       if letter in guessmade:
        main_word = main_word +letter

       else:
        main_word = main_word + "_ "
       if main_word == word:
            print(main_word)
            print("You have been granted a pardon!!!!")
            break
          

       print("guess the words ", main_word)
       guess = input()

       if guess in valid_entry:
        guessmade = guessmade + guess 
       else:
        print("Enter valid character") 
        guess = input() 

# Welcome the Player and ask to enter their name
name = input("Please enter your name gallowman: -->")
print("Welcome", name,"Who's for hanging today!")
print("=======================================")
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