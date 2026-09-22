import json

# Read private expense data
with open("data/expenses.json", "r") as file:
    expenses = json.load(file)

print("Personal Expense Assistant")
print("--------------------------")

question = input("What do you want to know? ")

if "food" in question.lower():
    total = 0

    for expense in expenses:
        if expense["category"].lower() == "food":
            total += expense["amount"]

    print("Your total food expense is ₹", total)

elif "shopping" in question.lower():
    total = 0

    for expense in expenses:
        if expense["category"].lower() == "shopping":
            total += expense["amount"]

    print("Your total shopping expense is ₹", total)

else:
    print("Sorry, I don't understand that question yet.")