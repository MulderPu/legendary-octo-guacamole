def high(x):
    scores = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, 
         "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, 
         "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, 
         "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, 
         "y": 25, "z": 26}
    list = x.split(' ')
    result = []
    for item in list:
        temp = 0
        for i in item:
            temp += int(scores[i])
        if len(result) == 0:
            result = {'word': item, 'score': temp}
        else:
            if temp > result['score']:
                result = {'word': item, 'score': temp}
    return result['word']
print(high("man i need a taxi up to ubud"))

