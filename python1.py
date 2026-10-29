#electicity billing

units = int(input("Enter units: "))

if units <= 100:
    bill = units * 2
elif units <= 200:
    bill = 200 + (units - 100) * 3
else:
    bill = 500 + (units - 200) * 5

print("Electricity Bill: Rs.", bill)
