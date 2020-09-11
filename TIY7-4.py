toppings = []
while True:
    topping = input("Pizza toppings (put quit to stop): ")
    if(topping == "quit"): break
    print("Adding topping to your pizza!")
    toppings.append(topping)
