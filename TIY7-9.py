sandwich_orders = ["pastrami", "ham sandwich", "pastrami", "cold meat sandwich", "turkey sandwich", "pastrami"]
finished_sandwiches = []

print("The deli has run out of pastrami.")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

lenoflist = len(sandwich_orders)
while(lenoflist > 0):
    print(f"I made your sandwich {sandwich_orders[0]}")
    finished_sandwiches.append(sandwich_orders[0])
    sandwich_orders.remove(sandwich_orders[0])
    lenoflist = len(sandwich_orders)

for finished in finished_sandwiches:
    print(f"Finished making {finished}.")


