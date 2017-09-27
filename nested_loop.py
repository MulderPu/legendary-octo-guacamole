def upside_down_asterix_triangle(i):
    if i == 0:
        return 0
    else:
        print('X ' * (i))
        return upside_down_asterix_triangle(i - 1)

def asterix_triangle(i, t=0):
    if i == 0:
        return 0
    else:
        print('X ' * (t + 1))
        return asterix_triangle(i - 1,t + 1)

upside_down_asterix_triangle(5)
print('Welcome To Python Programing!')
asterix_triangle(5)
