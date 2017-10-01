scrabble_dict = {
    'a':'1',
    'b':'3',
    'c':'3',
    'd':'1',
    'e':'2',
    'f':'2',
    'g':'4',
    'h':'1',
    'i':'4',
    'j':'5',
    'k':'8',
    'l':'3',
    'm':'1',
    'n':'1',
    'o':'1',
    'p':'10',
    'q':'3',
    'r':'1',
    's':'1',
    't':'1',
    'u':'1',
    'v':'4',
    'w':'4',
    'x':'4',
    'y':'8',
    'z':'10'
}

print('Scrabble Game')
word = input('Enter a word:')

total=0
for i in word:
    if i in scrabble_dict:
       total += int(scrabble_dict[i])

print('Total: %s'%(total))
