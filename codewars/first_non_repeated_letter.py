def first_none_repeated_letter(string):
    list = []
    if string == "":
        return ''
    new_string = string.lower()
    for i in new_string:
        if not i in list:
            list.append(i)
    for i in list:
        if new_string.count(i) ==1:
            letter = i
            pos = [pos for pos,char in enumerate(new_string) if char == letter]
            for k in pos:
                return string[k]
    return ''


string= "sTreSS"

#first_none_repeated_letter(string)
print(first_none_repeated_letter(string))
