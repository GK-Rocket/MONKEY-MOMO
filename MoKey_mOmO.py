

import time

print("hello, welcome to MONKEY MOMO")

time.sleep(1)
name = input("what is your name? \n")

while name == "":
    print("you did not enter your name")
    name = input("what is your name? \n")


print("Hello", name , ", Welcome to MONKEY MOMO")




menu = "Momo, Chatpate, Chewmien"
drink_menu = "mango lassi, water, coke"
hid_menu = ["momo", "chatpate" ,"chewmien", "mango lassi", "water" ,"coke"]

price = 0

print("here is our menu \n",menu)
time.sleep(.5)
print("And here is our menu for drinks \n", drink_menu)
time.sleep(1)



def identify(hid_menu, order):
    
    order = order.lower() 
    
    words = order.strip()

    words = words.split()

    want_food = []



    for word in words: 
        if word in hid_menu:
            if word == "momo":
                want_food.append("momo")

            elif word == 'chatpate':
                want_food.append('chatpate')

            elif word == "chewmine":
                want_food.append('chewmine')
                
            elif word == "water":
                want_food.append('water')

            elif word == "coke":
                want_food.append('coke')

            elif word == "mango lassi":
                want_food.append('mango lassi')

    return want_food
    
    
        
order = input("What would you like to have today? \n")

hid_menu = ["momo", "chatpate" ,"chewmien", "mango lassi", "water" ,"coke"]

want_food = identify(hid_menu, order)


res=set(want_food)
fix_want = list()
for ele in want_food:
    if ele not in fix_want:
        fix_want.append(ele)

qtds = {}

for items in fix_want:
    qty = int(input(f"How many {items} do you want today\n"))
    qtds[items] = qty






def per_total(fix_want):

    price = 0

    for meal in fix_want:
        
        if meal == "mango lassi":
            price += 5 * qty

        elif meal == "water":
            price += 2 * qty

        elif meal == "coke":
            price += 3 * qty

        elif meal == "momo":
            price += 20 * qty

        elif meal == "chatpate":
            price += 10 * qty

        elif meal == "chewmine":
            price += 15 * qty

    return price



price = per_total(fix_want)




print(f"Your total is ${price}")
time.sleep(1)

print(f"Sounds good {name} sir, Your order of ${price} will be delivered soon")


