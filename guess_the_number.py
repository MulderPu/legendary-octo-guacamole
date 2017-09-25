import random

print('~~Number Guessing Game~~')
try:
    range = int(input('Enter a range of number for generate random number to start the game:'))
    rand = random.randint(1,range)
    guess = int(input('Enter a number from 1 to %i:'%(range)))
    
    i=1
    while (i):
        print()
        if guess == 0 or guess < 0:
            print('Give up? Try again next time!')
            break
        elif guess < rand:
            print('Number too small.')
            guess = int(input('Enter a number from 1 to %i:'%(range)))
        elif guess > rand:
            print('Number too large.')
            guess = int(input('Enter a number from 1 to %i:'%(range)))
        elif guess == rand:
            print('Congratulation. You made it!')
            break
except:
    print('Wrong Input.')
