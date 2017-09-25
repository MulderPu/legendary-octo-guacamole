def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print('Factorial of an input number')
print()
print('Enter \'x/X\' for exit.')
try:
    number = input('Enter a number:')
    i=1
    while(i):
        if number in ['x','X']:
            print('Thank You for using!')
            break
        elif int(number) < 0:
            print('Factorial of negative numbers doesn\'t exist ...')
            print()
            number = input('Enter a number:')
        elif int(number) >= 0:
            print('Factorial of %s is %s'%(number,factorial(int(number))))
            print()
            number = input('Enter a number:')
except ValueError:
    print('Wrong input.')
