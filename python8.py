#inventory reconciliation

opening = int(input("Opening stock: "))
received = int(input("Stock received: "))
sold = int(input("Stock sold: "))

closing = opening + received - sold

print("Expected Closing Stock:", closing)

if closing < 0:
    print("Stock record is invalid")
elif closing < 10:
    print("Stock is low")
else:
    print("Stock is sufficient")
