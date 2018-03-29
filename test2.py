'''import string

secret_word = 'apple'
letters_guessed = []

word_so_far = ''
for i in secret_word:
    if i in letters_guessed:
        word_so_far += i
    else:
        word_so_far += '_ '

print(word_so_far)

letters_not_guessed = ''
for i in string.ascii_lowercase:
    if i not in letters_guessed:
        letters_not_guessed += i

print(string.ascii_uppercase)'''
person = input('Enter your name: ')
print('Hello', person)
