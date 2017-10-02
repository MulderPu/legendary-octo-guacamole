def increment_string(string):
    last = string[-1:]
    try:
        if int(last):
            new_number = int(last) + int(1)
            string = string[:-1]
            string += str(new_number)
    except ValueError:
        string += str(1)
    return string
string = 'foobar1'
print(increment_string(string))
