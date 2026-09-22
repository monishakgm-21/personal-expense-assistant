import json

# TOOL 1: Read private expense data
def get_expenses():
    with open("data/expenses.json", "r") as file:
        return json.load(file)


# TOOL 2: Calculate category total
def get_category_total(expenses, category):
    total = 0

    for expense in expenses:
        if expense["category"].lower() == category.lower():
            total += expense["amount"]

    return total


# TOOL 3: Calculate overall total
def get_total(expenses):
    total = 0

    for expense in expenses:
        total += expense["amount"]

    return total


# TOOL 4: Find highest spending category
def get_highest_category(expenses):
    category_totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category not in category_totals:
            category_totals[category] = 0

        category_totals[category] += amount

    highest_category = max(
        category_totals,
        key=category_totals.get
    )

    return highest_category, category_totals[highest_category]


# AGENT
def agent(question):

    expenses = get_expenses()

    question = question.lower()

    # Multi-step task
    if "total" in question and (
        "highest" in question or "most" in question
    ):
        total = get_total(expenses)

        category, amount = get_highest_category(expenses)

        return (
            f"Your total spending is ₹{total}. "
            f"Your highest spending is on {category}: ₹{amount}"
        )

    # Food
    elif "food" in question:
        total = get_category_total(expenses, "Food")

        return f"You spent ₹{total} on food."

    # Shopping
    elif "shopping" in question:
        total = get_category_total(expenses, "Shopping")

        return f"You spent ₹{total} on shopping."

    # Transport
    elif "transport" in question:
        total = get_category_total(expenses, "Transport")

        return f"You spent ₹{total} on transport."

    # Total
    elif "total" in question:
        total = get_total(expenses)

        return f"Your total spending is ₹{total}."

    # Highest spending
    elif "highest" in question or "most" in question:
        category, amount = get_highest_category(expenses)

        return f"Your highest spending is on {category}: ₹{amount}"

    else:
        return "I don't have a suitable tool for this question."


# MAIN PROGRAM
print("Personal Expense AI Agent")
print("-------------------------")

question = input("What do you want to know? ")

answer = agent(question)

print("\nAgent:", answer)