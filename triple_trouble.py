# return 1 if num1 has 3 straight number and num2 has 2 straight number
def triple_double (num1, num2):
    triple = 0
    double = 0
    list1= [int(i) for i in str(num1)]
    list2= [int(j) for j in str(num2)]
    for i in range(len(list1)):
        if i+2 < len(list1):
            if list1[i] == list1[i+1]:
                if list1[i+1] == list1[i+2]:
                    triple = 1
                    break
        else:
            break

    for j in range(len(list2)):
        if j+1 < len(list2):
            if list2[j] == list2[j+1]:
                double = 1 
                break
        else:
            break

    if triple == 1 and double == 1:
        return 1
    else:
        return 0

num1 = int(input('Enter first number:'))
num2 = int(input('Enter second number:'))
print(triple_double(num1,num2))

