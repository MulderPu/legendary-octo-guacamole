def calculate_vegetable_category(broccoli=0, cabbage=0, french_bean=0):
    broccoli_price = float(0.8)
    cabbage_price = float(0.65)
    french_bean_price = float(0.35)

    total = (broccoli*broccoli_price)+(cabbage*cabbage_price)+(french_bean*french_bean_price)
    return total

def calculate_meat_category(chicken=0, beef=0,lamb=0):
    chicken_price = float(1.2)
    beef_price = float(3.5)
    lamb_price = float(3.8)

    total = (chicken*chicken_price)+(beef*beef_price)+(lamb*lamb_price)
    return total

def calculate_seafood_category(fish=0,crab=0,prawn=0):
    fish_price = float(1.5)
    crab_price = float(3.2)
    prawn_price = float(3.5)

    total = (fish*fish_price)+(crab*crab_price)+(prawn*prawn_price)
    return total

def print_choice():
    print('[M]eat Category.')
    print('[V]egetable Category.')
    print('[S]eafood Category.')
    print('[C]alculate Order.')
    print()

def get_vege_subtotal():
    try:
        cabbage = int(input('Cabbage (per 100gram):'))
    except ValueError:
        cabbage = 0

    try:
        french_bean = int(input('French bean (per 100gram):'))
    except ValueError:
        french_bean = 0

    try:
        broccoli = int(input('Broccoli (per 100gram):'))
    except ValueError:
        broccoli = 0
    subtotal = calculate_vegetable_category(broccoli,cabbage,french_bean) 
    return subtotal

def get_meat_subtotal():
    try:
        chicken = int(input('Chicken (per 100gram):'))
    except ValueError:
        chicken = 0

    try:
        beef = int(input('Beef (per 100gram):'))
    except ValueError:
        beef = 0

    try:
        lamp = int(input('Lamp (per 100gram):'))
    except ValueError:
        lamp = 0
    
    subtotal = calculate_meat_category(chicken,beef,lamp)
    return subtotal

def get_seafood_subtotal():
    try:
        fish = int(input('Fish (per 100gram):'))
    except ValueError:
        fish = 0

    try:
        prawn = int(input('Prawn (per 100gram):'))
    except ValueError:
        prawn = 0

    try:
        crab = int(input('Crab (per 100gram):'))
    except ValueError:
        crab = 0

    subtotal = calculate_seafood_category(fish,crab,prawn)
    return subtotal

print('Welcome to Google Grocery Store. What would you like to order?')
flag = 1
subtotal_meat = 0
subtotal_vege = 0
subtotal_sea = 0
while (flag):
    print_choice()
    selection = input('What will you like to do?')
    if selection in ['m','M']:
        print('Meat Category')
        subtotal_meat += get_meat_subtotal()
        print('Subtotal for Meat Category: %s'%(subtotal_meat))
        print()
    elif selection in ['v', 'V']:
        print('Vegetable Category')
        subtotal_vege += get_vege_subtotal()
        print('Subtotal for Vegetable Category: %s'%(subtotal_vege))
        print()
    elif selection in ['s','S']:
        print('Seafood Category')
        subtotal_sea += get_seafood_subtotal()
        print('Subtotal for Seafood Category: %s'%(subtotal_sea))
        print()
    elif selection in ['c','C']:
        print('Total: ',subtotal_meat+subtotal_vege+subtotal_sea)
        print('Thank You, please come again.')
        flag=0
    else:
        sys.exit('Wrong Input.')

