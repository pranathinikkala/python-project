#atm transaction

balance = 1000

deposit = int(input("Enter deposit amount: "))
balance = balance + deposit

withdraw = int(input("Enter withdrawal amount: "))

if withdraw <= balance and withdraw > 0:
    balance = balance - withdraw
    print("Withdrawal successful")
else:
    print("Invalid withdrawal")

print("Final Balance:", balance)
