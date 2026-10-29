#employee payroll

basic = float(input("Enter basic salary: "))

hra = basic * 0.20
da = basic * 0.10
gross = basic + hra + da
net = gross - basic * 0.05

print("Gross Salary:", gross)
print("Net Salary:", net)
