#event budget calculation

venue = float(input("Venue cost: "))
food = float(input("Food cost: "))
other = float(input("Other expenses: "))
sponsorship = float(input("Sponsorship amount: "))
students = int(input("Number of participants: "))

total = venue + food + other
remaining = total - sponsorship

print("Total Expenses:", total)

if remaining <= 0:
    print("Sponsorship covers all expenses")
elif students > 0:
    print("Fee per student:", round(remaining / students, 2))
else:
    print("No participants available to share the cost")
