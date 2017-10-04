def reverse_words(str):
    list = str.split(' ')
    new_list = []
    for i in list:
        new_list.append(i[::-1])
    new_str = ' '.join(new_list)
    return new_str
str = "An example!"
print(reverse_words(str))
