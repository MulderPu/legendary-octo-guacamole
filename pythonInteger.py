user_input = input('Please enter an integer: ')

try:
    n = int(user_input)
except ValueError:
    print('I am afraid that %s is not an integer. Please try again.' %user_input)
else:
    n = int(user_input)
    nn = int(user_input+user_input)
    nnn = int(user_input+user_input+user_input)
    nnnn = int(user_input+user_input+user_input+user_input)

    print(n+nn+nnn+nnnn)

