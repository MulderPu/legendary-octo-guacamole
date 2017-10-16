def cakes(recipe, available):
    cake=[]
    for i in recipe:
        if i in available:
            cake.append(int(int(available[i])/int(recipe[i])))
        else:
            return 0
    return int(min(cake))

recipe = {"flour": 500, "sugar": 200, "eggs": 1, "apple":3}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
print(cakes(recipe, available))
