sandwich_orders = ["ham sandwich", "cold meat sandwich", "turkey sandwich"]
finished_sandwiches = []


lenoflist = len(sandwich_orders)
while lenoflist > 0:
    print(f"I made your sandwich {sandwich_orders[0]}")
    finished_sandwiches.append(sandwich_orders[0])
    sandwich_orders.remove(sandwich_orders[0])
    lenoflist = len(sandwich_orders)

for finished in finished_sandwiches:
    print(f"Finished making {finished}.")


