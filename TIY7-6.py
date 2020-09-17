toppings = []
active = True
while active:
    topping = input("Pizza toppings (put quit to stop): ")
    if topping == "quit": break
    print("Adding topping to your pizza!")
    toppings.append(topping)
    if len(toppings) > 7: active = False
