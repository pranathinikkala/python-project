#fuel cost calculation

distance = float(input("Enter distance in km: "))
mileage = float(input("Enter mileage in km/litre: "))
price = float(input("Enter fuel price per litre: "))

if distance >= 0 and mileage > 0 and price >= 0:
    fuel = distance / mileage
    cost = fuel * price

    print("Fuel Required:", round(fuel, 2), "litres")
    print("Travel Cost: Rs.", round(cost, 2))
else:
    print("Invalid input")
