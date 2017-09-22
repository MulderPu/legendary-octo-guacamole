print('Fibonacci Series')
try:
    start_value = int(input('Enter the start value for Fibonacci:'))
    end_value = int(input('Enter the end value for Fibonacci:'))

    a = start_value
    print(a)
    b = 1
    c = 0
    i = 0
    while (i!=1):
        c = a+b
        if c < end_value:
            print(c)
        else:
            i = 1
        b = a
        a = c
except ValueError:
    print('Wrong Input.')
    
    
