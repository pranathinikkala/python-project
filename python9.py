#food waste calculation

prepared = int(input("Meals prepared: "))
served = int(input("Meals served: "))

if prepared > 0 and 0 <= served <= prepared:
    waste = prepared - served
    percentage = waste / prepared * 100

    print("Wasted Meals:", waste)
    print("Waste Percentage:", round(percentage, 2), "%")
else:
    print("Invalid input")
