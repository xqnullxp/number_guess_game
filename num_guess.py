#wrote by null
#kys 
#im big haxxer man

import random

number = random.randint(1, 100)

while True:
    guess = int(input('\003[31menter shit from 1-100: '))

    if guess < number:
        print('\033[31mguess higher faggot')

    elif guess > number:
        print('\033[31mguess lower faggot')

    elif guess == number:
        print('\033[35mwow you actually got it faggot')