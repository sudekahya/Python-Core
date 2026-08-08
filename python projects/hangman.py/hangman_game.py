import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |
=========''']

from hangman_words import word_list

lives = 6

chosen_word = random.choice(word_list)


placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
  print(f"****************************{lives}/6 LIVES LEFT****************************")
  guess = input("guess a letter: ").lower()

  if guess in correct_letters:
    print(f"you have already guessed {guess}")

  display = ""

  for letter in chosen_word:
      if letter == guess:
         display += letter
         correct_letters.append(guess)

      elif letter in correct_letters:
         display += letter
         
      else:
         display += "_"
        
  if guess not in chosen_word:
    lives -= 1
    print(f"you guessed {guess}, that is not in the word. you lose a life")
    if lives == 0:
      game_over = True 
      print("you lose")


  if "_" not in display:
     game_over = True
     print("you win")

  print(stages[lives])
  print(display)
