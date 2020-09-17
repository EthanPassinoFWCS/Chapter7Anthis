number = 0
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid number.")
    exit(1)

if number % 10 == 0: print("Is a multiple of 10.")
else: print("Is not a multiple of 10.")

