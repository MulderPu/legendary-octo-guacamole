def spin_words(sentences):
    lists = sentences.split(' ')
    print(lists)
    for i in range(len(lists)):
        if len(lists[i]) >= 5:
            new_words = lists[i][::-1]
            lists[i] = new_words
    new_sentence = ' '.join(lists)
    return new_sentence

sentences = input('Enter sentences:')
print(spin_words(sentences))
