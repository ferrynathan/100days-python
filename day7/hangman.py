# Step 4

import random


def lire_mots(nom_fichier):
    """fonction qui récupère la liste des mots dans un fichier

    paramètre
      - nom_fichier, de type chaine de caractère : nom du fichier contenant les mots
        (un par ligne)

    retour : liste de chaine de caractères
    """
    liste_mots = []				# le tableau qui contiendra les lignes
    f = open(nom_fichier, encoding="UTF-8")  # on ouvre le fichier
    # une variable temporaire pour récupérer la ligne courante dans le fichier f
    ligne = f.readline()
    while ligne != "":
        # on rajoute la ligne courante dans le tableau
        liste_mots.append(ligne.strip())
        ligne = f.readline()                # on récupère la ligne suivante
    return liste_mots


stages = [
    '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
'''
]

end_of_game = False
user_score = 7
#word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(lire_mots("littre.txt"))
chosen_word = chosen_word.lower()
word_length = len(chosen_word)

# TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
# Set 'lives' to equal 6.

# Testing code
#print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

print(display)

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    correct_guess = 0
    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
            correct_guess += 1
    if correct_guess == 0:
        user_score -= 1
        print(f"User score = {user_score}")
        print(stages[user_score])

    # TODO-2: - If guess is not a letter in the chosen_word,
    # Then reduce 'lives' by 1.
    # If lives goes down to 0 then the game should stop and it should print "You lose."

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if user_score == 0:
        end_of_game = True
        print("You lose.")
        print(f"The word was {chosen_word}")
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
