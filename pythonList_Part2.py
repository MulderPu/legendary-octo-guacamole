#practice list part 2

num_list = [[11,12,13], [45,55,56], [10,11,12], [71,28,94]]

print('Output 1:',num_list[0] + num_list[3])
print('Output 2:',num_list[3] + num_list[1])

output3 = set([num_list[0][2]])
print('Output 3:', list(output3))

output4 = set([num_list[2][0]])
print('Output 4:',list(output4))

list = []
list.append(num_list[0])
list.append(num_list[1])
list.append(num_list[2])
list.append(num_list[1])
list.append(num_list[2])
print("Output 5:",list)
