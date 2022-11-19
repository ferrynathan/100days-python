print("Bienvenue au rollercoaster")
taille = int(input("Merci d'entrer votre taille en cm: "))

if taille >= 120:
    print("Ok pour la taille")
    age = int(input("Merci d'entrer votre age: "))
    if age < 12:
        ticket = 7
    elif age < 18:
        ticket = 10
    elif age >= 45 and age <= 50:
        ticket = 0
    else:
        ticket = 12
    photo = input(
        "Voulez-vous une photo de votre tour de manège ? Entrer O ou N:  ")
    if photo == "O":
        ticket += 3
    print(f"Vous allez devoir payer {ticket} euros.")
else:
    print("Désolé, vous êtes trop petit")
