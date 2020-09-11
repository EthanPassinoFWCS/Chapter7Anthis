poll_results = {}
users = ["Jake", "James", "Hallie", "Ethan", "Amy"]

for user in users:
    poll_results[user] = input("If you could visit one place in the world, where would you go? ")
    print("Thank you for taking our poll!")

print("\n")

for (user, place) in poll_results.items():
    print(f"If {user} could vist any place in the world, they would go to {place}!")

