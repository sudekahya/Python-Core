import random

rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper = ("""
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
""")

scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

your_choice = input("what do you choose?type 0 rock, 1 for paper or 2 for scissors.\n")

computer_choice = random.randint(0, 2)
print(f"computer chose {computer_choice}")

if your_choice == "0":
    print(rock)
    if computer_choice == 2:
        print(scissors)
        print("you win")
    elif computer_choice == 1:
        print(paper)
        print("you lose")
    else:
        print(rock)
        print("try again")

elif your_choice == "1":
    print(paper)
    if computer_choice == 0:
        print(rock)
        print("you win")
    elif computer_choice == 2:
        print(scissors)
        print("you lose")
    else:
        print(paper)
        print("try again")

elif your_choice == "2":
    print(scissors)
    if computer_choice == 1:
        print(paper)
        print("you win")
    elif computer_choice == 0:
        print(rock)
        print("you lose")
    else:
        print(scissors)
        print("try again")

else:
    print("invalid input")
