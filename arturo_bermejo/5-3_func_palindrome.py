word = input("Ingresa una palabra: ")

def is_palindrome(word):
    i = 0
    while i < len(word)/2:
        if word[i] != word[len(word)-i-1]:
            return False
        i += 1
    return True

if is_palindrome(word):
    print('Es palindromo')
else:
    print('No es palindromo')