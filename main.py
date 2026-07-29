import random
word_list = ["monkey", "beach", "coffee", "sugar"]

chosen_word = random.choice(word_list)
print(chosen_word)

guess = input("guess a letter: ").lower()
print(guess)

if guess in chosen_word:
    print("Right")
else:
    print("Wrong")