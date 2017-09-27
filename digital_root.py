n = 1234
print(sum(int(x) for x in str(n)))

num=0
for x in str(n):
    num += int(x)
print(num)
