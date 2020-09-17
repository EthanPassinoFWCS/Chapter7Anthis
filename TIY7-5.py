while True:
    age = 0
    try:
        age = int(input("What is your age? "))
        if age < 3: print("The cost of your movie ticket is free.")
        elif 3 <= age <= 12: print("The cost of your movie ticket is $10.")
        elif age > 12: print("The cost of your movie ticket is $15.")

    except ValueError:
        print("Invalid number.")
        exit(1)
