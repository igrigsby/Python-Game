import random
import sys

words = ['strong','confident','wise']
guess = ''
chances = 8

print('This is the Hangman game.\n In order to win you will have to guess the correct word')

word = random.choice(words)
print('The word has %s letters' %(len(word)))

guess = str(input('Please guess a letter: '))

while len(guess) != 1:
    print('Invalid entry. Please try again.')
    guess = str(input('Please guess a letter: '))

while chances > 1:
    failed = 0
    for char in word:
        if char in guess:
            print(char)
        else:
            print('_')
            failed += 1
    if failed == 0:
        print('good guess')
        break
    guesses = str(input('Please guess a letter: '))
    guess += guesses
    if guess not in word:
        chances -= 1
        print('Incorrect')
        print('You now have %s chances' %chances)
        
    if chances == 0:
        print('You lose')
    if len(word) == guess:
        print('You have won the game')





