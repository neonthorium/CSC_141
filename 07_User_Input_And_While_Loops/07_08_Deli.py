sandwich_orders = ['tuna', 'ham', 'cheese', 'veggie', 'pastrami', 'turkey', 'pastrami', 'roast beef', 'pastrami']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"\nI'm making your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print(f"\nI made your {sandwich} sandwich.")