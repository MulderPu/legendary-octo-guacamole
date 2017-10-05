def mix(s1, s2):
    s1 = sorted(s1, key=str.lower)
    s2 = sorted(s2, key=str.lower)
   
    list1 = []
    list2 = []
    for i in s1:
        if i not in list1 and i != ' ':
            list1.append(i)

    for j in s2:
        if j not in list2 and j != ' ' and j!= ',':
            list2.append(j)
            
    string = ''
    for a in list1:
        if a in s1:
            count1 = s1.count(a)
            if a in s2:
                count2 = s2.count(a)
                if count1 > count2:
                    if count1 > 1:
                        string += "1:"+a*count1+"/"
                elif count2 > count1:
                    if count2 > 1:
                        string += "2:"+a*count2+"/"
                elif count1 == count2:
                    if count1 > 1 and count2 > 1:
                        string += "=:"+a*count1+"/"
                
    return string

s1 = "Are they here"
s2 = "yes, they are here"
#print(s1.count('e'))

print(mix(s1,s2))
print('Ans :','2:eeeee/2:yy/=:hh/=:rr')
