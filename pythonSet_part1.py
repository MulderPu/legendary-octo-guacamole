'''
Write a Python program to create a symmetric difference.
Sample data: setx = set(["apple", "mango", "banana", "watermelon"])
sety = set(["mango", "orange","watermelon", "kiwi"])
'''
setx = set(["apple", "mango", "banana", "watermelon"])
sety = set(["mango", "orange","watermelon", "kiwi"])
print(setx.symmetric_difference(sety))
