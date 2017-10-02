def increment_string(string):
    last = string[-1:]
    try:
        if int(last):
            print(last)
            new_number = int(last) + int(1)
            string = string[:-1]
            string += str(new_number)
    except ValueError:
        print('err',last)
        string += str(1)
    return string
string = 'foobar00'

s="0"
if int(s):
    print('this is a number')
print(increment_string(string))
