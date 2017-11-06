def order(sentence):
    if not sentence:
        return ""
    new_list = []
    list = sentence.split() 
  
    for i in range(1,10):
        for item in list:
            if str(i) in item:
                 new_list.append(item)
    return " ".join(new_list)

sentence = 'is2 Thi1s T4est 3a'
print(order(sentence))
