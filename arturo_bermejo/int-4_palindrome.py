word = input("Ingresa una palabra: ")

i = 0
is_palindrome = True

while i < len(word)/2:
    if word[i] != word[len(word)-i-1]:
        is_palindrome = False
    i += 1

if is_palindrome:
    print('Es palindromo')
else:
    print('No es palindromo')

# simple way
# word == word[::-1]
