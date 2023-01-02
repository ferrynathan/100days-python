def greet():
    print("Hello !")
    print("Welcome to my home !")
    print("I'm Drakuul")


greet()

# name est le paramètre
# Nathan est l'argument


def greet_with_input(name):
    print(f"Hello {name}!")
    print("Welcome to my home !")
    print("I'm Drakuul")


greet_with_input("Nathan")


def greet_with_2_inputs(name, location):
    print(f"Hello {name}!")
    print(f"What are you doing in {location}?")


# positional arguments
greet_with_2_inputs("Nathan", "Bordeaux")

# keywords arguments
greet_with_2_inputs(location="Bordeaux", name="Nathan")
