#shopping bill

price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))

total = price * quantity

if total >= 1000:
    total = total * 0.90

print("Final Bill: Rs.", total)
