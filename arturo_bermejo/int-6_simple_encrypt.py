encrypt_dict = {
    'a': '9',
    'e': '3',
    'i': '0',
    'o': '8',
    'u': '1'
}

word = input("Ingresa una palabra: ")

for letter in encrypt_dict:
    word = word.replace(letter, encrypt_dict[letter])

print("La palabra encryptada es: " + word)
