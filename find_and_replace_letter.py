print('~Find and Replace~')
phrase = input('Enter a phrase:')
find_letter = input('Enter a letter to find:')
replace_letter = input('Enter a letter to replace:')
new_phrase = phrase.replace(find_letter,replace_letter)

print('Original phrase: %s'%(phrase))
print('New phrase: %s'%(new_phrase))

lists = ([i for i,char in enumerate(phrase) if char == find_letter])
print('%s appeared %s times in the phrase.'%(find_letter, len(lists)))
print('%s appeared at position:'%(find_letter),'~'.join(str(e) for e in lists))

