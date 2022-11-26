import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

list_of_choice = [rock, paper, scissors]
my_choice = input("What do you chose ? Type rock, paper or scissors: ")
print("You chose:")
if my_choice == "rock":
    print(rock)
elif my_choice == "paper":
    print(paper)
elif my_choice == "scissors":
    print(scissors)
computer_choice = random.choice(list_of_choice)
print("Computer chose:")
print(computer_choice)

if computer_choice == rock and my_choice == "rock":
    print("Even match !")
elif computer_choice == rock and my_choice == "scissors":
    print("Computer wins !")
elif computer_choice == rock and my_choice == "paper":
    print("Player wins !")
elif computer_choice == paper and my_choice == "rock":
    print("Computer wins !")
elif computer_choice == paper and my_choice == "scissors":
    print("Player wins !")
elif computer_choice == paper and my_choice == "paper":
    print("Even match !")
elif computer_choice == scissors and my_choice == "paper":
    print("Computer wins !")
elif computer_choice == scissors and my_choice == "rock":
    print("Player wins !")
elif computer_choice == scissors and my_choice == "scissors":
    print("Even match !")
