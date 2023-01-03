alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(text, shift):
    encrypted_word = ""
    for letter in text:
        position = alphabet.index(letter)
        new_position = position + shift
        if new_position > 25:
            new_position = new_position - 26
        encrypted_word += alphabet[new_position]
    print(f"Your encrypted word is {encrypted_word}")


encrypt(text, shift)
