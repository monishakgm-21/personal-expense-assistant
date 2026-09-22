import json

# Read the private expense data
with open("data/expenses.json", "r") as file:
    expenses = json.load(file)

print("Personal Expense - Rule Based Workflow")
print("---------------------------------------")

# Calculate total spending
total = 0

for expense in expenses:
    total = total + expense["amount"]

print("Total spending: ₹", total)

# Calculate spending by category
category_totals = {}

for expense in expenses:
    category = expense["category"]
    amount = expense["amount"]

    if category not in category_totals:
        category_totals[category] = 0

    category_totals[category] = category_totals[category] + amount

print("\nCategory-wise spending:")

for category, amount in category_totals.items():
    print(category, ": ₹", amount)

# Fixed rules
print("\nRules:")

for category, amount in category_totals.items():

    if amount > 1000:
        print(category, "→ High spending")

    elif amount > 500:
        print(category, "→ Moderate spending")

    else:
        print(category, "→ Normal spending")