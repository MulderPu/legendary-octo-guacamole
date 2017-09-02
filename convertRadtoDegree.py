'''
Write a Python program to accept a Radian value and convert into Degree value.
Test data:
Radian: .52
Expected output: 29.781818181818185
Note: pi = 22/7  
Formula: degree = radian * (180/pi)
'''

pi = 22/7

def convertRadToDegree(radian):
    degree = radian * (180/pi)
    return degree

user_input = input("Please enter a radian value to convert to degree:")

radian = float(user_input)

print(convertRadToDegree(radian))
